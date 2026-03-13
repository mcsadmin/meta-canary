# Prepared Commit Messages

These are the three commit messages ready to apply to the `meta-canary` repository,
following the mandatory verbose commit protocol from `07_coding_agent_master_prompt.md`.

---

## Commit 1 — Project scaffold, database module, and login behaviour

**Subject:**
```
Scaffold Flask project structure with SQLite database module and login behaviour
```

**Body:**
```
Added the initial project structure for the Local Loop QR Code Generator under
/code, including app.py (Flask application factory and all route definitions),
db.py (SQLite connection management via Flask's application context), requirements.txt,
a .gitignore excluding the database file and virtual environments, and a README with
local run and Railway deployment instructions.

This scaffold was required as the foundation for all seven confirmed behaviours; the
login route (Behaviour 1) is implemented first because every other route depends on
the authentication guard — unauthenticated requests are redirected to /login for all
protected paths.

The application factory pattern (create_app()) was chosen over a module-level app
object so that the SECRET_KEY and APP_PASSWORD are read from environment variables at
startup rather than at import time, keeping secrets out of source code and module state;
Flask's g object and teardown_appcontext are used to manage one SQLite connection per
request lifecycle.

Uncertainty: the spec does not specify a session lifetime beyond "until the browser is
closed"; Flask's default session cookie (session.permanent = False) matches this
requirement, but if a persistent session is needed in future, this will need revisiting.

No deviations from the specification. APP_PASSWORD and SECRET_KEY are read exclusively
from environment variables and are not present in any committed file.
```

---

## Commit 2 — QR code generation and history view

**Subject:**
```
Implement QR code generation (Behaviour 2) and history view (Behaviour 3) with SQLite persistence
```

**Body:**
```
Added the /generate POST route, which accepts a URL and label from an authenticated
user, generates a QR code using the qrcode library with Pillow as the image backend,
inserts a record into the qr_codes SQLite table (id, label, url, created_at), and
redirects to the new QR code's detail page; the index route (GET /) now queries all
rows ordered by creation date descending and renders them in the history table.

These two behaviours are the core value of the tool — without generation and history,
nothing else is useful — and they share the same database write/read cycle, making them
natural to implement together.

SQLite with WAL journal mode was chosen for persistence, as specified; the DB_PATH
environment variable allows the file to be placed on a Railway persistent volume without
code changes. The qrcode library generates a PIL image object which is serialised to a
BytesIO buffer and served directly for the inline preview on the detail page, avoiding
any filesystem writes for the image data itself.

Concern: qrcode's default error correction level (M) is used; if QR codes are to be
printed at very small sizes, level H might be preferable, but the spec does not specify
a size or use-case constraint so the default is retained.

No deviations from the specification. URL validity checking is explicitly out of scope
per the spec brief and has not been implemented.
```

---
