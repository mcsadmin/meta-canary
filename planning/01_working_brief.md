# Local Loop Experiment Week — The Working Brief
### 12–17 March 2026 | Dil's Home, London

---

## 1. Who and Where

**Tom** and **Dil** are working together at Dil's home in London from Wednesday 12 March to Tuesday 17 March 2026. Tom has travelled from Liverpool. The week is a co-located, intensive experiment. Tom returns to Liverpool on Tuesday 17 March.

---

## 2. Direction and Vision

### 2.1 The Experiment Vision

> *Validated confidence that Tom and Dil can build products of equivalent complexity and ambition to the sandbox project being built this week — putting them back in the driving seat on the tech roadmap and massively reducing third-party dependency.*

The experiment is a de-risking exercise, not a delivery commitment. The question being answered is: **can we do this?** — not "have we done it?" The answer is expected to be yes, but the experiment is designed to produce evidence, not assertion.

The longer-term North Star is on-premises, self-hosted AI: no dependency on cloud providers. The experiment week is the first step toward that.

### 2.2 The Platform Vision

> *Build a robust, accurate, and reliable graph of local obligations on a real-time basis — the best achievable approximation to a source of truth for the local economy, which can be leveraged to provide useful insights and actionable analysis, of which clearing is only the first example.*

Local Loop is a graph-building project. The obligation graph — businesses as nodes, invoices as edges — is the primary artefact. Clearing is a query on the graph; it is not the graph itself. This distinction is the single most important framing decision made in the pre-experiment planning.

---

## 3. The Sandbox Target

The minimum viable end-of-week output is a **working sandbox** of Local Loop that is:

- Up and running and accessible at `sandbox.localloop-merseyside.co.uk`
- On GitHub, in a well-structured repository
- Well-documented, with all key artefacts in place
- Passing its defined automated tests
- Using the functional prototype UI as the front end
- Playable by real users — Tom, Dil, Paul, and Yanny at minimum

The sandbox is not a production system. It is not a claim that Local Loop is built. It is evidence that the approach works and that the platform can be built at the level of ambition required.

---

## 4. The "Build the Graph" Framing

This is the in-session testable constraint that governs every scope decision during the week:

> *"Does this \<x\> contribute to the delivery of a graph that is robust, accurate, and reliable as a source of truth about the local economy, which can be leveraged to provide useful insights and actionable analysis — of which clearing is only the first example?"*

If the answer is no — if a feature or requirement consumes the graph rather than building it — it goes in the MoSCoW parking lot. This test can be applied by either Tom or Dil in the moment, without requiring a formal boundary call.

---

## 5. MoSCoW Scope

The MoSCoW framework governs all scope decisions during the week. Both Tom and Dil have full rights and responsibilities to invoke it. The parking lot is a first-class artefact — ideas go in, not out.

**Must Have (MVP — the sandbox target):**
- A working obligation graph with verified nodes (the Directory / business directory component)
- A data pipeline that ingests dummy invoice data and populates the graph
- Automated test harnesses confirming the graph's integrity constraints
- Deployment to `sandbox.localloop-merseyside.co.uk`
- The functional prototype UI connected to the live graph
- A well-structured Git repository with all artefacts in place

**Should Have (if time and energy permit):**
- At least one analytical query on the graph (clearing as a worked example)
- Gitbook publication layer live and linked from the repository

**Could Have (post-experiment backlog):**
- Additional analytical queries
- Real invoice data ingestion (replacing dummy data)
- The "little app" for method log management

**Won't Have (this week):**
- Production-grade security, key rotation, incident response
- Multi-tenant architecture
- Integration with live Xero or accounting platform data
- Any feature that consumes the graph without first building it

---

## 6. The Experiment Structure

The week is structured around six operational units, in sequence:

| Unit | When | Purpose |
|---|---|---|
| Meta-canary | Wednesday morning | Rehearse and validate the working method |
| Project canary (Directory) | Thursday | End-to-end build of the verified nodes component |
| Requirements and specification sessions | Friday | BDD specifications, data model, test harnesses |
| Build sessions | Saturday–Monday | AI-agent-directed coding within defined scope |
| Review and testing sessions | Throughout | Verify integrity constraints and test coverage |
| Deployment | Monday–Tuesday | Deploy sandbox to confirmed domain |

---

## 7. The Working Method in Summary

The working method is governed by the VSM design document (v5). The key principles for daily operation are:

**Before each session:** agree a session charter (one to two sentences: what we are producing, what is out of scope, T-shirt size of any build work). Deliver to the coaching agent.

**During each session:** apply the "build the graph" test to every scope question. Invoke MoSCoW when needed. Raise a capture signal when something needs to be made visible. Raise a course-correction signal if the session is not working.

**At the end of each warm conversation:** produce a handoff note (three to five bullet points: what was decided, what was parked, what the next session needs to address). Deliver to the coaching agent.

**At the end of each day:** send the end-of-day signal to the coaching agent. Review the daily state document (five minutes). Confirm or flag the anti-loop check assessment.

**Sunday late afternoon/early evening:** the midpoint review — full conversation, transcript delivered to the coaching agent for second-half rolling plan.

---

## 8. Paul and Yanny

Paul and Yanny are not involved as direct reviewers during the experiment. The agreed approach:

- **Daily progress summaries** via the daily state document (coaching agent generates; Tom and Dil share).
- **Exception-based calls** for genuine blocks that Paul or Yanny have specific knowledge to resolve.
- **Input on key architectural choices before the main build begins.** The graph database question — relational only, hybrid, or pure graph — must be resolved with Paul and Yanny before the main build starts. This is a Day Zero item.

---

## 9. The Closing Protocol

The experiment ends on Tuesday 17 March. The closing protocol is a standard retrospective using the format Tom and Dil are already familiar with. The coaching agent generates a closing state document in advance. The retrospective is the mechanism by which the experiment's learning is converted into a strategic decision about the future of Local Loop development.

---

*This document is the authoritative single working brief for the Local Loop experiment week. It should be the first document read by any new AI instance working on the experiment. It is stored in `/planning/01_working_brief.md` in the experiment repository.*

*Prepared by Manus AI, 12 March 2026.*
