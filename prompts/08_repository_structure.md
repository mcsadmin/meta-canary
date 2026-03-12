# Local Loop Experiment Week — Repository Structure
### Ready to Initialise During the Meta-Canary

---

## Overview

All artefacts produced during the experiment week live in a **single Git repository**. This document defines the agreed folder structure, the ownership model, and the initialisation steps to be completed during the meta-canary.

---

## Folder Structure

```
local-loop-experiment/
│
├── /code                    # The Local Loop sandbox build
│   ├── /core                # The obligation graph and integrity constraints
│   └── /modules             # Data pipeline, directory, analytical queries
│
├── /specs                   # BDD specifications, data model, NFR documents
│   ├── /features            # Gherkin feature files
│   ├── /data-model          # Node and edge schemas, integrity constraints
│   └── /nfr                 # Non-functional requirement specifications
│
├── /tickets                 # Tickets generated from the BDD process
│   ├── /backlog             # Not yet started
│   ├── /in-progress         # Currently being worked
│   └── /done                # Completed and verified
│
├── /planning                # Working brief, VSM map, rolling plan documents
│   ├── 01_working_brief.md
│   ├── 02_vsm_map.md
│   └── rolling_plan/        # Daily rolling plan documents
│
├── /method                  # Working method protocol, daily state documents
│   ├── 03_working_method_protocol.md
│   └── daily_state/         # Daily state documents (AI-generated)
│
├── /log                     # The method log bucket (raw capture)
│   ├── charters/            # Session charter records
│   ├── handoffs/            # Handoff note records
│   ├── signals/             # Course-correction and capture signal records
│   └── observations/        # Free-form method log entries
│
├── /artefacts               # Diagrams, Mermaid files, whiteboard photos/scans
│   ├── /mermaid             # .mmd source files
│   ├── /rendered            # Rendered PNG/SVG diagrams
│   └── /photos              # Whiteboard photos and scans
│
└── /prompts                 # Named AI task prompts (versioned, refinable)
    ├── 04_coaching_master_prompt.md          # Pre-meta-canary version
    ├── 04_coaching_master_prompt_v2.md       # Post-meta-canary version (to be created)
    ├── 05_session_charter_prompt.md
    ├── 06_handoff_note_prompt.md
    ├── 07_coding_agent_master_prompt.md
    ├── 08_repository_structure.md            # This document
    ├── daily_state_document_prompt.md        # To be created during meta-canary
    ├── anti_loop_check_prompt.md             # To be created during meta-canary
    ├── blind_spot_check_prompt.md            # To be created during meta-canary
    ├── gap_analysis_prompt.md                # To be created during meta-canary
    ├── method_log_processing_prompt.md       # To be created during meta-canary
    └── health_check_prompt.md               # To be created during meta-canary
```

---

## Directory Ownership

| Directory | Primary Controller | Coaching Agent Access |
|---|---|---|
| `/code` | Tom, Dil, coding agents | Read (monitoring) |
| `/specs` | Tom, Dil, coding agents | Read (monitoring, gap analysis) |
| `/tickets` | Tom, Dil, coding agents | Read (monitoring) |
| `/prompts` | Tom, Dil (with agent proposals) | Read + propose updates |
| `/planning` | Coaching agent | Read + write |
| `/method` | Coaching agent | Read + write |
| `/log` | Coaching agent (writes structure); Tom & Dil (write raw entries) | Read + write |
| `/artefacts` | Coaching agent (writes diagrams); Tom & Dil (write photos/scans) | Read + write |

---

## Domains

| Environment | Domain | Purpose |
|---|---|---|
| Meta-canary | `meta-canary.commoner.services` | Method rehearsal (QR code generator) |
| Project canary | `canary.commoner.services` | Directory / verified nodes component |
| Main sandbox | `sandbox.localloop-merseyside.co.uk` | Full Local Loop sandbox |

---

## Initialisation Steps (to be completed during the meta-canary)

Complete these steps in order during the meta-canary session:

**Step 1 — Create the repository**
```bash
git init local-loop-experiment
cd local-loop-experiment
```

**Step 2 — Create the folder structure**
```bash
mkdir -p code/core code/modules
mkdir -p specs/features specs/data-model specs/nfr
mkdir -p tickets/backlog tickets/in-progress tickets/done
mkdir -p planning/rolling_plan
mkdir -p method/daily_state
mkdir -p log/charters log/handoffs log/signals log/observations
mkdir -p artefacts/mermaid artefacts/rendered artefacts/photos
mkdir -p prompts
```

**Step 3 — Add placeholder README files**

Create a `README.md` in each top-level directory with one sentence describing its purpose. This ensures the folder structure is committed and navigable from day one.

**Step 4 — Copy the briefing documents**

Copy all eight briefing documents from the design task into their correct locations:
- `01_working_brief.md` → `/planning/`
- `02_vsm_map.md` → `/planning/`
- `03_working_method_protocol.md` → `/method/`
- `04_coaching_master_prompt.md` → `/prompts/`
- `05_session_charter_prompt.md` → `/prompts/`
- `06_handoff_note_prompt.md` → `/prompts/`
- `07_coding_agent_master_prompt.md` → `/prompts/`
- `08_repository_structure.md` → `/prompts/`

**Step 5 — Initial commit**
```bash
git add .
git commit -m "Initialise repository structure

Eight-directory structure created as agreed in the VSM design session.
All briefing documents from the design task copied into their correct locations.
Prompts directory contains pre-meta-canary versions of all prompts that must
exist before the meta-canary; remaining prompts will be created during the
meta-canary and committed as part of its outputs.
No code yet — this is the structural foundation for the experiment week."
```

**Step 6 — Push to GitHub and set up the publication layer**

Push to a new GitHub repository. Set up Gitbook (or equivalent) with native GitHub integration. Confirm the publication layer is live and accessible at a single URL before proceeding with the meta-canary warm conversation.

---

## The Publication Layer

**Recommended:** Gitbook, connected to the GitHub repository via native integration. Gitbook renders Markdown files as a navigable documentation site with minimal configuration.

**Confirm during meta-canary:** the publication layer is live, the repository structure is visible, and the working brief is readable at the published URL.

**Purpose:** single addressable URL for all experiment artefacts; vehicle for sharing daily state documents with Paul and Yanny; persistent record of the experiment for post-experiment review.

---

## Commit Message Standard

All commits — from coding agents and from Tom and Dil — follow this standard:

**Subject line:** one sentence, present tense, describing what the commit does.

**Body:** five to six sentences covering:
1. What was done
2. Why it was done
3. Design decisions made
4. Concerns or uncertainties
5. Deviations from specification (if any)

This standard is mandatory. The coaching agent reads the commit log as its primary signal of build progress. Thin commit messages degrade monitoring quality.

---

*This document is stored in `/prompts/08_repository_structure.md` in the experiment repository.*

*Prepared by Manus AI, 12 March 2026.*
