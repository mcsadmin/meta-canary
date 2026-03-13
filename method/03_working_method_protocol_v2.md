# Local Loop Experiment Week — Working Method Protocol
### Single-Page Operational Reference | Version 2 (post-meta-canary)

---

## The Rhythm

Every unit of work follows the same loop:

```
MORNING BRIEFING (5 min) → SESSION CHARTER (3 min) → WARM WORK → HANDOFF NOTE (5 min) → COLD AI PROCESSING → REVIEW (5 min) → NEXT SESSION
```

**End of day:** send the end-of-day signal → review daily state document (5 min) → sign off anti-loop check.

---

## Start of Day — The Morning Briefing

At the start of each new day, before any session charter, the coaching agent produces a **morning briefing** — a short, warm summary covering: where we are, what happened yesterday, what today looks like, and any flags worth knowing before we start. Read it over coffee. It is not a formal document; it is a handover from the previous day's cold processing to the new day's warm work.

*The coaching agent commits the morning briefing to `/method/daily_state/morning_briefing_YYYY-MM-DD.md`.*

---

## Before Every Session — The Session Charter

Agree in one to two sentences and deliver to the coaching agent:

- **What** we are producing in this session (one specific output)
- **What is out of scope** (at least one thing explicitly excluded)
- **T-shirt size** of any build work: 20 min / 45 min / 90 min

*The coaching agent proposes a draft charter from the rolling plan. Confirm or adjust in the first three minutes. In the early sessions, the agent will briefly explain why it is proposing each step — this scaffolding reduces as the team becomes fluent.*

---

## During Every Session — The In-Session Tests

**The "build the graph" test** — apply to every scope question:
> *"Does this contribute to a graph that is robust, accurate, and reliable as a source of truth about the local economy, which can be leveraged to provide useful insights and actionable analysis?"*
> If no → MoSCoW parking lot.

**The MoSCoW boundary call** — either Tom or Dil can invoke at any time. Both have full authority. If inconclusive → S2-C (disagreement protocol).

**The session clock** — the coaching agent notes elapsed time at natural breakpoints. Not rigid, but enough to keep pace visible.

---

## The Two Signals

**Capture signal** — triggered when something needs to be made visible (structural insight, architectural decision, domain constraint, process observation). Does not stop the session. Medium is flexible: whiteboard photo or dump to AI agent for Mermaid diagram. Output goes to `/artefacts`.

**Course-correction signal** — triggered by any of these six conditions:
1. Build session produces no artefact after allocated T-shirt time
2. AI output cannot be understood or verified
3. Disagreement unresolved after one cold processing cycle
4. Daily state document flags build more than one day behind rolling plan
5. Either Tom or Dil feels the experiment is not working
6. Coaching agent consistently producing unhelpful outputs

When triggered: **stop immediately** → 15-minute meta-conversation → coaching agent proposes three options → choose one → record in method log.

---

## After Every Warm Conversation — The Handoff Note

Three to five bullet points, delivered by Tom and Dil to the coaching agent:
- What was **decided**
- What was **parked** (and why)
- What the **next session** needs to address

**The coaching agent prompts for these bullet points — it never writes them.** The handoff note content must come from Tom and Dil. The coaching agent structures the note, surfaces implications, and commits it to `/log/`.

*Keep conversations short enough that key points are not forgotten.*

---

## End of Day — The Batch Signal

Send one message to the coaching agent: **"End of day — please run the batch."**

The coaching agent runs: method log processing → daily state document → anti-loop check → blind spot check → gap analysis → health check.

Review the daily state document (5 min). Respond to the anti-loop check: **"agreed"** or **"flagged — discuss tomorrow."**

---

## Technical Design Decisions

When a technical choice is unavoidable, the coaching agent must surface it explicitly as a named decision, present options, and wait for positive confirmation before proceeding. The coaching agent does not make technology choices on behalf of the team.

---

## Parallel Working

As the project grows, the coaching agent will signal moments when Tom and Dil can work on independent streams simultaneously. When signalled, the agent will be specific about what can be done in parallel and why there is no conflict. Do not assume parallel working is possible until it is explicitly signalled.

---

## The Method Log Bucket

Drop anything relevant into `/log` — voice-note transcripts, typed observations, signal records, whiteboard photo references. Maximum two minutes per entry. Format does not matter. The coaching agent structures it.

---

## The Sunday Midpoint Review

Sunday late afternoon or early evening. Full conversation — the transcript goes to the coaching agent. Agenda:
- Is the working method working?
- Is the build on track for the sandbox target?
- What needs to change for the final two days?

---

## The Disagreement Protocol (S2-C)

When Tom and Dil reach genuine disagreement: state it explicitly (one sentence each) → park in method log → coaching agent elicits resolution in cold processing → resolve in next warm session. Written record to repo.

---

## Git Discipline

Every commit from a coding agent must have a verbose message body (5–6 sentences):
- What was done and why
- Design decisions made
- Concerns or uncertainties
- Deviations from specification or agreed architecture

**The coding agent must be able to make direct commits to the repository.** Confirm this before the coding session begins. If the chosen tool cannot commit directly, discuss the workaround with Tom and Dil before starting.

Process decisions compound through Git via protocol updates — this protocol is a versioned document.

---

## What the Coaching Agent Does NOT Do

The coaching agent does not generate more than approximately one page of technical content. When a task exceeds this boundary, it frames a brief and hands off:
- Sustained BDD/Gherkin writing → subsidiary Manus task
- Code generation, debugging → coding agent

The coaching agent does not make technical design decisions. It does not write handoff note content. It does not proceed without human confirmation on scope or architecture questions.

---

*This protocol is stored in `/method/03_working_method_protocol_v2.md`.*
*Version 2 produced as a meta-canary output, 13 March 2026.*
*Version 1 (pre-meta-canary baseline) is preserved at `/method/03_working_method_protocol.md`.*
