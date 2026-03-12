# Specification Brief — Meta-Canary QR Code Generator
### For the Coding Agent | 12 March 2026

---

## What You Are Building

A simple, private, internal QR code generator for the MCS and Local Loop team. It is not a public service. It is a lightweight web application that allows the team to generate, store, label, view, export, and delete QR codes that encode URLs directly.

**Deployed to:** `meta-canary.commoner.services` (Railway)

---

## Architecture

| Layer | Technology |
|---|---|
| **Application** | Python — Flask |
| **Persistence** | SQLite (single file, stored on Railway persistent volume) |
| **Hosting** | Railway free tier, deployed from GitHub |
| **Password control** | Single shared team password, stored as a Railway environment variable |

This is a simple server-rendered application. There is no separate front-end framework. Flask serves HTML templates directly. Keep it simple and debuggable.

---

## Confirmed Behaviours

Implement the following seven behaviours and no others:

1. **Login** — A user visits the app and is presented with a password form. On entering the correct password, they are granted access. On entering an incorrect password, they are shown an error. The session persists via a cookie until the browser is closed.
2. **Generate** — An authenticated user enters a URL and a label, and submits the form. The app generates a QR code that encodes the URL directly, stores the QR code (with its label, URL, and creation timestamp) in the SQLite database, and displays the new QR code on screen.
3. **View history** — An authenticated user can view a list of all previously generated QR codes, showing the label, URL, and creation date for each.
4. **Select** — An authenticated user can select a specific QR code from the history to view it in full.
5. **Export as PNG** — From the selected QR code view, the user can download the QR code as a PNG file.
6. **Export as SVG** — From the selected QR code view, the user can download the QR code as an SVG file.
7. **Delete** — From the selected QR code view, the user can delete the QR code. A simple confirmation step is required before deletion (e.g., a confirmation button or prompt). The record is removed from the database permanently.

---

## Out of Scope

- URL validity checking — the app does not validate whether the URL is well-formed or reachable
- QR code redirect approach — the QR code encodes the URL directly; there is no redirect layer
- Multi-user authentication — one shared team password only
- Any feature not listed in the seven behaviours above

---

## Non-Functional Requirements

| NFR | Requirement |
|---|---|
| **Security** | Password stored as environment variable — never hardcoded in source or committed to Git |
| **Logging** | Log all significant operations (login attempts, QR generation, deletions) with basic context |
| **Documentation** | A README in `/code` explaining how to run the app locally and how to deploy to Railway |
| **Secrets** | No secrets in code or commit history |

---

## What the Coding Agent Is Expected to Produce

For the meta-canary, the goal is **not** a complete, production-ready application. The goal is a small number of working commits that demonstrate the commit protocol and show the working method functioning end-to-end.

**Minimum expected output:**
- At least two to three commits, each with a verbose message body (see commit protocol below)
- A working Flask application that implements at least behaviours 1 and 2 (login and generate)
- A SQLite database schema committed to the repository
- A README with basic run instructions

**Stretch goal (if time permits):**
- Behaviours 3, 4, 5, 6, and 7 implemented and working locally

---

## Commit Protocol — Mandatory

Every commit must have a verbose message body. Subject line: one sentence. Body: five to six sentences covering:

1. What was done
2. Why it was done
3. Design decisions made
4. Concerns or uncertainties
5. Deviations from this specification (if any)

Thin commit messages degrade the coaching agent's ability to monitor the build. This is not optional.

---

## Repository Location

Your code goes in `/code` in the `meta-canary` repository on GitHub (`https://github.com/mcsadmin/meta-canary`).

---

*Produced by Manus AI (Coaching Agent) | Session 4 | 12 March 2026*
*Pending confirmation by Tom and Dil before handoff to coding agent.*
