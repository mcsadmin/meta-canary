# Handoff Note Prompt
### Pre-Written Prompt for the Coaching Agent | Ready to Use at End of Each Warm Conversation

---

## How to Use This Prompt

At the end of each warm conversation, before handing off to the cold AI processing step, Tom and Dil produce a handoff note. The handoff note is the primary input to the coaching agent's synthesis — it is the human-curated signal that tells the agent what matters from the conversation.

**Hard rule:** The coaching agent never writes the content of a handoff note. The bullet points must come from Tom and Dil. The coaching agent's job is to prompt for them, then structure and commit what is provided.

**Step 1:** The coaching agent asks: *"Please give me three to five bullet points covering what was decided, what was parked, and what the next session needs to address."*

**Step 2:** Tom and Dil provide the bullet points. This takes no more than five minutes. Keep conversations short enough that key points are not forgotten.

**Step 3:** Paste the bullet points to the coaching agent along with the prompt below.

**Step 4:** The coaching agent structures the note, identifies implications, and writes it to the `/log` bucket.

This prompt is stored in `/prompts/06_handoff_note_prompt.md`. It will be revised during the meta-canary if needed.

---

## The Prompt

```
HANDOFF NOTE

Here are our notes from the session we just completed:

[PASTE YOUR BULLET POINTS HERE]

Please do the following:

1. Acknowledge the decisions made and confirm you have understood them correctly.
2. Identify any implications of these decisions that we may not have surfaced — particularly any that affect the rolling plan, the MoSCoW scope, or the "build the graph" test.
3. Flag any items that should go into the method log (process observations, concerns, what worked, what didn't).
4. Propose a session charter for the next session, based on what we have just decided and the current rolling plan.
5. Write the structured handoff note to /log/ with the filename format: handoff_YYYY-MM-DD_HH.md

Keep your response concise. If you have concerns, flag them clearly but briefly.
```

---

## What a Good Handoff Note Contains

The coaching agent's structured output should cover:

| Section | Content |
|---|---|
| **Decisions made** | What was agreed, with enough context to be unambiguous |
| **Items parked** | What was explicitly set aside, and why |
| **Implications** | Anything the decisions imply that was not explicitly discussed |
| **Method log flags** | Any process observations worth capturing |
| **Next session charter (draft)** | One to two sentences proposing the next session's focus |

---

## Example Input (for reference)

Tom and Dil's bullet points after a data model session:

> - Agreed: nodes are businesses (registered UK companies), identified by Companies House number
> - Agreed: edges are invoices — directed, from supplier to customer, with amount, date, and status
> - Parked: whether to include sole traders — too much data quality complexity for the canary
> - Parked: real-time vs. batch ingestion — decision needed before build sessions start
> - Next: write the node schema as a formal spec, then move to integrity constraints

---

*Prepared by Manus AI, 12 March 2026.*
