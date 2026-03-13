"""
QR Code Generator — Flask application entry point and route definitions.

All seven confirmed behaviours from the spec brief are implemented here:
  1. Login  (GET/POST /login, POST /logout)
  2. Generate  (POST /generate)
  3. View history  (GET /)
  4. Select  (GET /qr/<id>)
  5. Export as PNG  (GET /qr/<id>/export/png)
  6. Export as SVG  (GET /qr/<id>/export/svg)
  7. Delete  (POST /qr/<id>/delete)

Secrets are read exclusively from environment variables:
  - APP_PASSWORD  : the shared team password
  - SECRET_KEY    : Flask session signing key
"""

import io
import logging
import os
import sys

import qrcode
import qrcode.image.svg
from flask import (
    Flask,
    flash,
    redirect,
    render_template,
    request,
    send_file,
    session,
    url_for,
)

from db import close_db, get_db, init_db

# ---------------------------------------------------------------------------
# Logging — structured, to stdout so Railway / any 12-factor host captures it
# ---------------------------------------------------------------------------
logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s — %(message)s",
)
log = logging.getLogger("qr_generator")

# ---------------------------------------------------------------------------
# Application factory
# ---------------------------------------------------------------------------

def create_app() -> Flask:
    app = Flask(__name__)

    secret_key = os.environ.get("SECRET_KEY")
    if not secret_key:
        raise RuntimeError(
            "SECRET_KEY environment variable is required but not set. "
            "Set it before starting the application."
        )
    app.secret_key = secret_key

    with app.app_context():
        init_db()

    app.teardown_appcontext(close_db)

    # -----------------------------------------------------------------------
    # Auth helpers
    # -----------------------------------------------------------------------

    def _app_password() -> str:
        pwd = os.environ.get("APP_PASSWORD")
        if not pwd:
            raise RuntimeError(
                "APP_PASSWORD environment variable is required but not set."
            )
        return pwd

    def _authenticated() -> bool:
        return session.get("authenticated") is True

    def _require_auth():
        if not _authenticated():
            return redirect(url_for("login"))
        return None

    # -----------------------------------------------------------------------
    # Behaviour 1 — Login / Logout
    # -----------------------------------------------------------------------

    @app.route("/login", methods=["GET", "POST"])
    def login():
        if _authenticated():
            return redirect(url_for("index"))

        if request.method == "POST":
            entered = request.form.get("password", "").strip()
            ip = request.remote_addr
            if entered == _app_password().strip():
                session["authenticated"] = True
                log.info("Login successful — ip=%s", ip)
                return redirect(url_for("index"))
            else:
                log.warning("Login failed (wrong password) — ip=%s", ip)
                flash("Incorrect password. Please try again.", "error")

        return render_template("login.html")

    @app.route("/logout", methods=["POST"])
    def logout():
        session.clear()
        log.info("User logged out — ip=%s", request.remote_addr)
        return redirect(url_for("login"))

    # -----------------------------------------------------------------------
    # Behaviour 3 — View history (index / home)
    # -----------------------------------------------------------------------

    @app.route("/")
    def index():
        guard = _require_auth()
        if guard:
            return guard

        db = get_db()
        rows = db.execute(
            "SELECT id, label, url, created_at FROM qr_codes ORDER BY created_at DESC"
        ).fetchall()
        return render_template("index.html", qr_codes=rows)

    # -----------------------------------------------------------------------
    # Behaviour 2 — Generate
    # -----------------------------------------------------------------------

    @app.route("/generate", methods=["POST"])
    def generate():
        guard = _require_auth()
        if guard:
            return guard

        url = request.form.get("url", "").strip()
        label = request.form.get("label", "").strip()

        if not url or not label:
            flash("Both a URL and a label are required.", "error")
            return redirect(url_for("index"))

        db = get_db()
        cursor = db.execute(
            "INSERT INTO qr_codes (label, url) VALUES (?, ?)",
            (label, url),
        )
        db.commit()
        new_id = cursor.lastrowid
        log.info("QR code generated — id=%s label=%r url=%r", new_id, label, url)
        flash(f'QR code "{label}" created successfully.', "success")
        return redirect(url_for("view_qr", qr_id=new_id))

    # -----------------------------------------------------------------------
    # Behaviour 4 — Select / view a single QR code
    # -----------------------------------------------------------------------

    @app.route("/qr/<int:qr_id>")
    def view_qr(qr_id: int):
        guard = _require_auth()
        if guard:
            return guard

        db = get_db()
        row = db.execute(
            "SELECT id, label, url, created_at FROM qr_codes WHERE id = ?",
            (qr_id,),
        ).fetchone()
        if row is None:
            flash("QR code not found.", "error")
            return redirect(url_for("index"))

        return render_template("view_qr.html", qr=row)

    # -----------------------------------------------------------------------
    # Behaviour 5 — Export as PNG
    # -----------------------------------------------------------------------

    @app.route("/qr/<int:qr_id>/export/png")
    def export_png(qr_id: int):
        guard = _require_auth()
        if guard:
            return guard

        db = get_db()
        row = db.execute(
            "SELECT url, label FROM qr_codes WHERE id = ?", (qr_id,)
        ).fetchone()
        if row is None:
            flash("QR code not found.", "error")
            return redirect(url_for("index"))

        img = qrcode.make(row["url"])
        buf = io.BytesIO()
        img.save(buf, format="PNG")
        buf.seek(0)
        filename = f"{_safe_filename(row['label'])}.png"
        log.info("PNG export — id=%s label=%r", qr_id, row["label"])
        return send_file(buf, mimetype="image/png", as_attachment=True, download_name=filename)

    # -----------------------------------------------------------------------
    # Behaviour 6 — Export as SVG
    # -----------------------------------------------------------------------

    @app.route("/qr/<int:qr_id>/export/svg")
    def export_svg(qr_id: int):
        guard = _require_auth()
        if guard:
            return guard

        db = get_db()
        row = db.execute(
            "SELECT url, label FROM qr_codes WHERE id = ?", (qr_id,)
        ).fetchone()
        if row is None:
            flash("QR code not found.", "error")
            return redirect(url_for("index"))

        factory = qrcode.image.svg.SvgPathImage
        qr_img = qrcode.make(row["url"], image_factory=factory)
        buf = io.BytesIO()
        qr_img.save(buf)
        buf.seek(0)
        filename = f"{_safe_filename(row['label'])}.svg"
        log.info("SVG export — id=%s label=%r", qr_id, row["label"])
        return send_file(buf, mimetype="image/svg+xml", as_attachment=True, download_name=filename)

    # -----------------------------------------------------------------------
    # Behaviour 7 — Delete (with confirmation step via POST)
    # -----------------------------------------------------------------------

    @app.route("/qr/<int:qr_id>/delete", methods=["POST"])
    def delete_qr(qr_id: int):
        guard = _require_auth()
        if guard:
            return guard

        confirmed = request.form.get("confirm") == "yes"
        if not confirmed:
            flash("Deletion was not confirmed. The QR code was not deleted.", "error")
            return redirect(url_for("view_qr", qr_id=qr_id))

        db = get_db()
        row = db.execute(
            "SELECT label FROM qr_codes WHERE id = ?", (qr_id,)
        ).fetchone()
        if row is None:
            flash("QR code not found.", "error")
            return redirect(url_for("index"))

        db.execute("DELETE FROM qr_codes WHERE id = ?", (qr_id,))
        db.commit()
        log.info("QR code deleted — id=%s label=%r", qr_id, row["label"])
        flash(f'QR code "{row["label"]}" has been permanently deleted.', "success")
        return redirect(url_for("index"))

    return app


# ---------------------------------------------------------------------------
# Utility
# ---------------------------------------------------------------------------

def _safe_filename(label: str) -> str:
    """Return a filesystem-safe version of the label for download filenames."""
    safe = "".join(c if c.isalnum() or c in "-_ " else "_" for c in label)
    return safe.strip().replace(" ", "_") or "qr_code"


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app = create_app()
    app.run(host="0.0.0.0", port=port, debug=False)
