"""
Database module — SQLite connection management and schema initialisation.

Uses Flask's application context (g) to maintain a single connection per
request. The database file path defaults to 'qr_codes.db' in the working
directory; override with the DB_PATH environment variable (useful for Railway
persistent-volume mounts).
"""

import os
import sqlite3

from flask import g

DB_PATH = os.environ.get("DB_PATH", "qr_codes.db")

SCHEMA = """
CREATE TABLE IF NOT EXISTS qr_codes (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    label      TEXT    NOT NULL,
    url        TEXT    NOT NULL,
    created_at TEXT    NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ', 'now'))
);
"""


def get_db() -> sqlite3.Connection:
    """Return the SQLite connection for the current application context."""
    if "db" not in g:
        g.db = sqlite3.connect(DB_PATH, detect_types=sqlite3.PARSE_DECLTYPES)
        g.db.row_factory = sqlite3.Row
        g.db.execute("PRAGMA journal_mode=WAL;")
    return g.db


def close_db(exception=None) -> None:
    """Close the SQLite connection at the end of the request."""
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db() -> None:
    """Create tables if they do not already exist."""
    db = get_db()
    db.executescript(SCHEMA)
    db.commit()
