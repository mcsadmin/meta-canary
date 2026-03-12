# Session Charter Prompt
### Pre-Written Prompt for the Coaching Agent | Ready to Use at Meta-Canary Start

---

## How to Use This Prompt

Copy the prompt below and deliver it to the coaching agent at the start of any warm conversation or build session. The coaching agent will respond with a draft session charter for Tom and Dil to confirm or adjust. The confirmed charter is written to the `/log` bucket by the coaching agent.

This prompt is stored in `/prompts/05_session_charter_prompt.md`. It will be revised during the meta-canary if needed.

---

## The Prompt

```
SESSION CHARTER REQUEST

Please propose a session charter for the session we are about to begin.

A session charter is one to two sentences covering:
1. The specific output this session is intended to produce (one concrete deliverable)
2. What is explicitly out of scope for this session (at least one thing)
3. The T-shirt size of any build work planned: 20 minutes / 45 minutes / 90 minutes (omit if this is a planning or conversation session)

Base your proposal on:
- The current rolling plan (from the most recent daily state document in /method/)
- Any handoff note from the previous session (in /log/)
- The current MoSCoW status

Present the charter as a single short paragraph, followed by a one-line scope exclusion statement.

After presenting the draft, ask: "Does this reflect what you want to do in this session, or would you like to adjust it?"

Once confirmed, write the agreed charter to /log/ with the filename format: charter_YYYY-MM-DD_HH.md
```

---

## Example Output (for reference)

> **Session charter — 13 March 2026, 10:00**
>
> This session will produce a confirmed data model for the Directory (verified nodes) component, covering the node schema, the key integrity constraints, and the relationship types needed for the obligation graph. We are not writing Gherkin scenarios or touching code in this session.
>
> *Out of scope: any discussion of the invoice data pipeline or clearing queries.*
>
> Does this reflect what you want to do in this session, or would you like to adjust it?

---

*Prepared by Manus AI, 12 March 2026.*
