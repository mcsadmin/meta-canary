# Local Loop Experiment Week — Coding Agent Master Prompt
### Opening Brief for Cursor / Claude Code / Replit

---

## How to Use This Document

This document is the opening brief for any AI coding agent (Cursor, Claude Code, Replit, or equivalent) working on the Local Loop experiment week. Read it in full before writing any code. It covers: what you are building, how to work, and what is expected of every commit.

---

## What You Are Building

You are building a **working sandbox** of Local Loop — a graph-based platform that maps local business obligations in the local economy. The sandbox will be deployed to `sandbox.localloop-merseyside.co.uk`.

### The Platform in One Sentence

Local Loop builds a **robust, accurate, and reliable graph of local obligations** — businesses as nodes, invoices as edges — that can be queried to provide useful insights and actionable analysis of the local economy.

### The "Build the Graph" Test

Before implementing any feature, ask: *"Does this contribute to the delivery of a graph that is robust, accurate, and reliable as a source of truth about the local economy?"* If the answer is no, do not build it. Flag it to Tom or Dil instead.

### The Sandbox Target

The minimum viable output is a system that is:
- Up and running at `sandbox.localloop-merseyside.co.uk`
- On GitHub, in a well-structured repository
- Passing its defined automated tests
- Using the functional prototype UI as the front end
- Playable by real users

---

## The Architecture Principles

### Core vs. Modules

The codebase is structured as a **core** (the obligation graph and its integrity constraints) with **modules** (the data pipeline, the directory, the analytical queries). The core must be stable before modules are built. Do not build modules that depend on an unstable core.

### Well-Factored, Not Microservices

The code should be well-factored and modular — clean separation of concerns, clear interfaces between components — but it is **not** a distributed microservices architecture. Independent deployment of services is not a goal for the sandbox. Debuggability and clarity are.

### Graph Database Decision

The graph database architecture (relational only, hybrid relational/graph, or pure graph) will be confirmed with Paul and Yanny before the main build begins. Do not make this decision unilaterally. If you are asked to implement a data model before this decision is confirmed, flag it.

### Non-Functional Requirements (NFRs)

The following NFRs are mandated from day one — they are not to be bolted on later:

| NFR | Requirement |
|---|---|
| **Logging** | Structured logging on all significant operations; errors must be logged with context |
| **Testing** | Automated test harnesses for all integrity constraints; no untested constraint is a confirmed constraint |
| **Accessibility** | UI components must meet WCAG 2.1 AA as a minimum |
| **Internationalisation** | String externalisation from day one; do not hardcode user-facing strings |
| **Documentation** | Every module must have a README; every public function must have a docstring |
| **Security** | No secrets in code or commit history; environment variables for all credentials |

---

## The BDD Approach

Requirements are written in Gherkin format (Given / When / Then). Tickets are generated from the BDD specifications. Your job is to implement the tickets, not to interpret the requirements. If a ticket is ambiguous, flag it — do not resolve ambiguity silently.

Specifications are in `/specs`. Tickets are in `/tickets`. Your code goes in `/code`.

---

## The Commit Protocol — This Is Mandatory

Every commit must have a **verbose message body**. The subject line is one sentence. The body is five to six sentences covering:

1. **What was done** — the specific change made
2. **Why it was done** — the reasoning or requirement it addresses
3. **Design decisions made** — any choices between alternatives, and why this one was chosen
4. **Concerns or uncertainties** — anything you are not confident about, or that might need review
5. **Deviations from specification** — any place where the implementation differs from the spec or agreed architecture, and why

**This is not optional.** The coaching agent reads the commit log as its primary signal of what is happening in the build. Thin commit messages degrade the coaching agent's ability to monitor the experiment and flag problems early.

### Example Commit Message

```
Add node schema for business directory (verified nodes)

Implemented the Business node schema with Companies House number as the 
primary identifier, as agreed in the data model session. Used a UUID as 
the internal graph node ID to decouple from the external identifier.

Chose to store the Companies House number as a string rather than an 
integer to handle leading zeros correctly — this was not in the spec but 
is a known UK data quality issue.

Uncertain about the indexing strategy for the Companies House number field; 
have added a basic index but this may need review once we have realistic 
data volumes.

No deviation from the agreed schema; the sole trader exclusion decision 
(parked in handoff note 2026-03-14) means this schema only covers 
registered companies for now.
```

---

## Commit Frequency

Commit **often** — at least at the end of every meaningful unit of work, and whenever you have something working that you do not want to lose. Small, frequent commits with verbose bodies are far more useful than large, infrequent commits with thin messages.

---

## Direct Commit Requirement

You must be able to make **direct commits to the repository**. This is a hard requirement — the coaching agent reads the commit log as its primary signal of what is happening in the build, and this only works if commits land in the repository in real time.

Before starting any coding session, confirm that your tool can push directly to GitHub. If it cannot (e.g., due to platform policy), flag this to Tom and Dil before starting. Do not begin a coding session without resolving this. If a workaround is agreed, document the deviation clearly in every commit message body.

---

## What to Do When Stuck

If you are stuck — the code is not working, the specification is ambiguous, or you are uncertain about an architectural decision — **stop and flag it**. Do not spend more than the allocated T-shirt time (20/45/90 minutes) without producing a working artefact. Write a commit with a message body explaining what you tried and why it did not work, then flag the issue to Tom or Dil.

---

## Repository Structure

```
/code          — your work goes here
/specs         — BDD specifications and data model (read these)
/tickets       — your implementation targets (read these)
/planning      — working brief and VSM map (read these before starting)
/method        — working method protocol and daily state documents
/log           — method log bucket (do not write here directly)
/artefacts     — diagrams and visual artefacts
/prompts       — AI task prompts
```

---

*This prompt is stored in `/prompts/07_coding_agent_master_prompt.md` in the experiment repository.*

*Prepared by Manus AI, 12 March 2026.*
