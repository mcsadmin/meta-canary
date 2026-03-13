# Local Loop QR Code Generator

A private, internal QR code generator for the MCS and Local Loop team.

---

## What it does

A simple Flask web application that lets the team generate, store, label, view, export, and delete QR codes that encode URLs directly. Password-protected via a single shared team password. All data stored in a local SQLite database.

### Features

1. **Login** — shared team password, session cookie
2. **Generate** — enter a URL and label; QR code is stored and displayed
3. **View history** — list of all QR codes with label, URL, and creation date
4. **Select** — view a single QR code in full
5. **Export as PNG** — download the QR code as a PNG file
6. **Export as SVG** — download the QR code as an SVG file
7. **Delete** — permanently delete a QR code (with confirmation step)

---

## Running locally

### Prerequisites

- Python 3.10+
- pip

### 1. Clone the repository

```bash
git clone https://github.com/mcsadmin/meta-canary.git
cd meta-canary/code
```

### 2. Create a virtual environment and install dependencies

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Set environment variables

**Never hardcode these values.** Set them in your shell before starting the app:

```bash
export APP_PASSWORD="your-team-password-here"
export SECRET_KEY="a-long-random-string-here"
```

Optionally, set `DB_PATH` to control where the SQLite file is written (defaults to `qr_codes.db` in the working directory):

```bash
export DB_PATH="/path/to/persistent/qr_codes.db"
```

### 4. Run the development server

```bash
python app.py
```

The app will be available at `http://localhost:5000`.

---

## Deploying to Railway

### Prerequisites

- A Railway account and the Railway CLI (`railway login`)
- A Railway project linked to this repository

### Steps

1. In the Railway dashboard, set the following environment variables for your service:
   - `APP_PASSWORD` — the shared team password
   - `SECRET_KEY` — a long random secret string
   - `DB_PATH` — path on the Railway persistent volume, e.g. `/data/qr_codes.db`
   - `PORT` — Railway sets this automatically; Flask reads it

2. Attach a **Volume** to the service and mount it at `/data` so the SQLite file survives redeploys.

3. Set the **Start Command** to:
   ```
   python app.py
   ```

4. Push to GitHub. Railway will deploy automatically on each push to the connected branch.

---

## Project structure

```
code/
├── app.py            # Flask application — all routes and app factory
├── db.py             # SQLite connection management and schema
├── requirements.txt  # Python dependencies
├── README.md         # This file
├── static/
│   └── style.css     # Application stylesheet (WCAG 2.1 AA compliant)
└── templates/
    ├── base.html     # Shared layout — navbar, flash messages
    ├── login.html    # Login page (Behaviour 1)
    ├── index.html    # History + generate form (Behaviours 2 & 3)
    └── view_qr.html  # Single QR view, export, delete (Behaviours 4–7)
```

---

## Security notes

- `APP_PASSWORD` and `SECRET_KEY` are **never** stored in source code or committed to Git.
- Always set them as environment variables in the host environment.
- The SQLite database file should be excluded from version control (it is listed in `.gitignore`).
- Session cookies are signed with `SECRET_KEY` using Flask's default HMAC signing.

---

*Internal tool — MCS and Local Loop team | Built March 2026*
