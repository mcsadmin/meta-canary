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

