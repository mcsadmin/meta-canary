# Local Loop Experiment Week — Working Method Protocol
### Single-Page Operational Reference | Version 1 (pre-meta-canary)

---

## The Rhythm

Every unit of work follows the same loop:

```
SESSION CHARTER (3 min) → WARM WORK → HANDOFF NOTE (5 min) → COLD AI PROCESSING → REVIEW (5 min) → NEXT SESSION
```

**End of day:** send the end-of-day signal → review daily state document (5 min) → sign off anti-loop check.

---

## Before Every Session — The Session Charter

Agree in one to two sentences and deliver to the coaching agent:

- **What** we are producing in this session (one specific output)
- **What is out of scope** (at least one thing explicitly excluded)
- **T-shirt size** of any build work: 20 min / 45 min / 90 min

*The coaching agent can propose a draft charter from the rolling plan. Confirm or adjust in the first three minutes.*

---

## During Every Session — The In-Session Tests

**The "build the graph" test** — apply to every scope question:
> *"Does this contribute to a graph that is robust, accurate, and reliable as a source of truth about the local economy, which can be leveraged to provide useful insights and actionable analysis?"*
> If no → MoSCoW parking lot.

**The MoSCoW boundary call** — either Tom or Dil can invoke at any time. Both have full authority. If inconclusive → S2-C (disagreement protocol).

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

Three to five bullet points, delivered to the coaching agent:
- What was **decided**
- What was **parked** (and why)
- What the **next session** needs to address

*This is the primary input to the coaching agent's synthesis. Keep conversations short enough that key points are not forgotten.*

---

## End of Day — The Batch Signal

Send one message to the coaching agent: **"End of day — please run the batch."**

The coaching agent runs: method log processing → daily state document → anti-loop check → blind spot check → gap analysis → health check.

Review the daily state document (5 min). Respond to the anti-loop check: **"agreed"** or **"flagged — discuss tomorrow."**

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

Process decisions compound through Git via protocol updates — this protocol is a versioned document.

---

## What the Coaching Agent Does NOT Do

The coaching agent does not generate more than approximately one page of technical content. When a task exceeds this boundary, it frames a brief and hands off:
- Sustained BDD/Gherkin writing → subsidiary Manus task
- Code generation, debugging → coding agent (Cursor, Claude Code, Replit)

---

*This protocol is stored in `/method/03_working_method_protocol.md`. It is updated by the coaching agent when process decisions are made. Version 1 is the pre-meta-canary baseline; Version 2 will be produced as a meta-canary output.*

*Prepared by Manus AI, 12 March 2026.*
