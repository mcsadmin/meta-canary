# Handoff Note — Session 5 | 13 March 2026

**Session:** Coding agent (Replit) — commits with rich messages
**Status:** Complete
**Note:** Human-authored by Tom and Dil.

---

## What Was Produced

- A working (though not perfect) application produced through the Replit coding agent process.
- Session secrets (`SECRET_KEY`) and team password (`APP_PASSWORD`) were created and saved.
- Three simulated commits landed in the repository, each with a verbose message body following the commit protocol. All seven behaviours are implemented.

---

## Issues Encountered

- **Replit direct commit policy:** Replit cannot make direct commits to external repositories. A workaround was found: code downloaded from Replit, committed manually using `git commit -F` with a `COMMIT_MESSAGES.md` file preserving Replit's intended commit messages. This is a significant finding for the working method — Replit is not a suitable coding agent for this workflow as currently designed without a modified integration approach.

- **Technical design decision not properly flagged:** The coaching agent proposed Flask as the application framework in Session 4 without explicitly labelling it as a design decision requiring validation. This was missed by Tom and Dil at the time. **The coaching agent's role should not include making technical design choices.** When a technical decision is unavoidable, the coaching agent must surface it explicitly, label it clearly as a design decision, and require a positive confirmation before proceeding. This must be addressed in the revised coaching master prompt v2.

---

## Items Parked

- Application quality — the app is working but not production-ready. Testing, code reviews, and UAT remain out of scope for the meta-canary.

---

## Next Session

- Session 6: review coding agent output.

---

## Implications Surfaced by Coaching Agent

- The `commitmsg.txt` file used during the commit process was committed to the root of the repository. This should be cleaned up (deleted and committed) before the repository is used further.
- The `.DS_Store` file in `/code` was also committed — a macOS artefact that should be in `.gitignore`. Worth a tidy-up commit.
- The three commits are marked as simulated in their message bodies, which is transparent and correct. The `COMMIT_MESSAGES.md` in `/artefacts/` serves as the permanent record of Replit's intended output.

---

*Human content provided by Tom and Dil | Structured by Manus AI (Coaching Agent) | 13 March 2026*
