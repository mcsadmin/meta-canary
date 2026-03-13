# Briefing Note: SUMMARY.md Discipline
### For the agent finalising the documentation update

---

## The Problem

This repository uses **GitBook** for publishing. GitBook does not automatically discover files in the repository — it only displays files that are explicitly listed in `SUMMARY.md`. Any file committed to the repository but absent from `SUMMARY.md` is **invisible in GitBook**, even though it exists in GitHub.

During the meta-canary experiment (12–13 March 2026), 20+ files were committed to the repository across two evenings of sessions. `SUMMARY.md` was only updated once (early on 12 March) and was not kept in sync with subsequent commits. As a result, the majority of the meta-canary record — all Day 2 charters, handoff notes, daily state documents, revised prompts, rolling plans, and artefacts — was invisible in GitBook.

This was discovered after the meta-canary closed and has been corrected manually (commit `f2be565`).

---

## What Was Done to Resolve It

`SUMMARY.md` was rewritten to include every `.md` file currently in the repository. The following categories of files were added:

| Category | Files Added |
|---|---|
| Rolling plans | 13 March v1 and v2 |
| Method | Working method protocol v2; daily state 13 March |
| Prompts | Coaching master prompt v2 |
| Log — charters | Sessions 6, 7, 9, 10 (13 March) |
| Log — handoff notes | Sessions 5, 6, 7, 8, 9 (13 March) |
| Artefacts | `COMMIT_MESSAGES.md` |
| Directories | README entries for log, method, planning, prompts, specs |

The updated `SUMMARY.md` is now committed and live.

---

## What Needs to Be Added to the Documentation

The following rule must be added to **two documents**:

### 1. `method/03_working_method_protocol_v2.md`

Add a new subsection under **Git Discipline** (or as a standalone subsection near it):

> **SUMMARY.md discipline**
>
> Every file committed to the repository must also be added as a line in `SUMMARY.md` in the same commit. Files not listed in `SUMMARY.md` are invisible in GitBook. This applies to all new files: session charters, handoff notes, daily state documents, rolling plans, specification briefs, artefacts, and prompt revisions.
>
> The coaching agent is responsible for including the `SUMMARY.md` update in every commit that adds a new file. This is not optional and should not be deferred to a later commit.

### 2. `prompts/08_repository_structure.md`

Add a note in the section describing the repository structure (wherever `SUMMARY.md` is mentioned or wherever the GitBook publishing setup is described):

> **Important:** `SUMMARY.md` is the single source of truth for GitBook navigation. Whenever a new file is added to the repository, a corresponding entry must be added to `SUMMARY.md` in the same commit. The format is:
>
> ```
> * [Human-readable title](path/to/file.md)
> ```
>
> Files committed without a `SUMMARY.md` entry will exist in GitHub but will not appear in GitBook.

---

## Summary for the Documentation Agent

- **Problem:** `SUMMARY.md` was not kept in sync with new commits during the meta-canary, causing most files to be invisible in GitBook.
- **Fix applied:** `SUMMARY.md` rewritten to include all current files (commit `f2be565`).
- **Rule to add:** "Every new file committed to the repository must have a `SUMMARY.md` entry in the same commit." This rule belongs in both `03_working_method_protocol_v2.md` (under Git Discipline) and `08_repository_structure.md` (near the GitBook/SUMMARY.md description).

---

*Prepared by Manus AI (Coaching Agent) | 13 March 2026*
