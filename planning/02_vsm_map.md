# Local Loop Experiment Week — The Confirmed VSM Map
### Reference Document for the Coaching Task

---

## Purpose of This Document

This document provides the structural foundation for the coaching AI task. It maps the experiment week against Stafford Beer's Viable System Model, making explicit which mechanisms serve which VSM function. Any AI instance coaching or monitoring the experiment week should read this document alongside the working brief and the working method protocol.

The experiment week functions as an **S4 process** within the wider Local Loop development system — it is the system's mechanism for rebuilding adaptive capacity and restoring the founders' ability to take back the technical driving seat. For the experiment week to fulfil this S4 function, it must itself be a viable system: all five VSM systems must be present and well-orchestrated.

---

## The Five Systems

### S5 — Identity and Policy

S5 holds the identity of the whole and sets the policy boundaries within which everything else operates.

| S5 Element | Statement |
|---|---|
| **Experiment vision** | Validated confidence that Tom and Dil can build products of equivalent complexity and ambition to the sandbox project being built this week |
| **Platform vision** | Build a robust, accurate, and reliable graph of local obligations on a real-time basis — the best achievable approximation to a source of truth for the local economy, which can be leveraged to provide useful insights and actionable analysis, of which clearing is only the first example |
| **Sandbox target** | A working, deployed, documented, tested, playable sandbox at `sandbox.localloop-merseyside.co.uk` |
| **Primary framing** | This is a "build the graph" project. Clearing is a query on the graph; it is not the primary artefact |
| **Policy boundary** | MoSCoW discipline governs all scope decisions |

### S4 — Environmental Intelligence and Adaptation

S4 scans the environment, models the future, and feeds intelligence back to S5 to enable adaptation.

| S4 Mechanism | Description |
|---|---|
| **Rolling two-day planning window** | Primary adaptation mechanism; generates a revised plan every two days based on current state |
| **T-shirt sizing** | Build sessions assigned 20/45/90 minute sizes; forces explicit effort estimation |
| **AI-facilitated elicitation** | Rolling plan generated through AI questioning, not prescription |
| **Warm-cold rhythm** | Structural pattern enabling S4 to function: warm conversation → handoff note → cold AI processing → outputs |
| **Daily blind spot check** | AI task: what has not been discussed that probably should have been? |
| **Daily gap analysis** | AI task: what was flagged as important but has not been addressed? |

### S3 — Resource Bargaining and Performance Management

S3 manages current operations and monitors performance against agreed targets.

| S3 Mechanism | Description |
|---|---|
| **Daily state document** | AI-generated, one page maximum; artefacts produced, MoSCoW status, rolling plan for next two days |
| **MoSCoW boundary call** | In-the-moment scope enforcement; both Tom and Dil have full authority; S2-C is the fallback if inconclusive |
| **"Build the graph" test** | In-session testable constraint; see working brief §4 |
| **Git discipline** | Verbose commit bodies (5–6 sentences); compounds code, specs, and process decisions |
| **Sunday midpoint review** | Full conversation transcript delivered to coaching agent; generates second-half rolling plan |

### S3* — The Audit Channel

S3* provides direct intelligence from S1 to S5, bypassing S3.

| S3* Mechanism | Description |
|---|---|
| **Course-correction signal** | Six defined trigger conditions; stops current work; 15-minute meta-conversation; three options proposed by coaching agent |
| **Capture signal** | Triggered when something needs to be made visible; flexible medium (whiteboard or AI agent); produces Mermaid diagram in `/artefacts` |
| **Method log bucket** | Capture-first, structure-later; raw entries in `/log`; coaching agent tags and synthesises at end of day |
| **Coaching AI health check** | Daily self-assessment by coaching agent; flags drift or degradation |

### S2 — Coordination and Anti-Oscillation

S2 prevents destructive oscillation between S1 units and between Tom and Dil.

| S2 Mechanism | Description |
|---|---|
| **Session charter** | 1–2 sentences before each session; what we are producing, what is out of scope, T-shirt size; coaching agent writes to repo |
| **Handoff note** | 3–5 bullet points at end of each warm conversation; what was decided, parked, and needed next; coaching agent writes to repo |
| **Disagreement protocol** | Backstop for genuine disagreements; state, park, refer to coaching agent; resolve in next warm session; also the fallback from inconclusive MoSCoW calls |
| **Anti-loop check** | Daily AI assessment of planning-to-building ratio; one paragraph; included in daily state document; Tom and Dil sign off |

### S1 — The Operational Units

| Unit | Domain | Hosted At |
|---|---|---|
| Meta-canary (QR code generator) | Method rehearsal | `meta-canary.commoner.services` |
| Project canary (Directory / verified nodes) | Business directory component | `canary.commoner.services` |
| Requirements and specification sessions | BDD specs, data model, test harnesses | Repository `/specs` and `/tickets` |
| Build sessions | AI-agent-directed coding | Repository `/code` |
| Review and testing sessions | Integrity verification, test coverage | Repository `/specs` and `/code` |
| Deployment | Sandbox deployment | `sandbox.localloop-merseyside.co.uk` |

---

## The Course-Correction Signal — Six Trigger Conditions

The coaching agent must be alert to all six conditions and surface them immediately if detected:

1. A build session produces no working code or specification artefact after the allocated T-shirt time has elapsed.
2. The AI coding tool produces output that Tom or Dil cannot understand or verify.
3. A disagreement between Tom and Dil cannot be resolved by the disagreement protocol within one cold processing cycle.
4. The daily state document flags that the build is more than one day behind the rolling plan.
5. Either Tom or Dil feels that the experiment is not working, for any reason.
6. The coaching agent is consistently producing unhelpful or generic outputs.

When triggered: stop the current session immediately; brief meta-conversation (15 minutes maximum); coaching agent proposes three options for how to proceed; Tom and Dil choose one; choice and reasoning recorded in the method log.

---

## The Handoff Boundary

The coaching agent must recognise when to hand off to a more appropriate agent:

| Task Type | Agent |
|---|---|
| Session charters, handoff notes, rolling plans, state documents, gap analyses, architectural framing, brief specification drafts | Coaching agent (this task) |
| Sustained BDD/Gherkin/Cucumber writing, data model specification, NFR documentation | Subsidiary Manus task |
| Code generation, test harness construction, ticket implementation, iterative debugging | Coding agent (Cursor, Claude Code, Replit) |

**Trigger:** when the coaching agent would need to produce more than approximately one page of generative technical content to complete a task, it frames the brief and hands off. It resumes its monitoring role when the output is committed to the repository.

---

## The End-of-Day Batch

All daily AI tasks are triggered by a single human end-of-day signal from Tom or Dil. The coaching agent runs all tasks in one pass:

1. Method log processing (tag and synthesise `/log` entries)
2. Daily state document (artefacts, MoSCoW status, rolling plan)
3. Anti-loop check (planning-to-building ratio assessment)
4. Daily blind spot check (what has not been discussed?)
5. Daily gap analysis (what was flagged but not addressed?)
6. Coaching AI health check (self-assessment)

Tom and Dil review the daily state document (five minutes) and sign off on the anti-loop check assessment.

---

## The Warm-Cold Rhythm

```
[Warm conversation] → [Handoff note] → [Cold AI processing] → [AI outputs to repo] → [Review] → [Next warm conversation]
```

The warm phase is human-led: Tom and Dil think, discuss, and decide. The cold phase is AI-led: the coaching agent structures, synthesises, and proposes. The handoff note is the bridge — the human-curated signal that tells the AI what matters.

---

*This document is stored in `/planning/02_vsm_map.md` in the experiment repository. It should be read alongside the working brief (01) and the working method protocol (03).*

*Prepared by Manus AI, 12 March 2026.*
