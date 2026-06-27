# Product Management Plugin

Product management practice for Carinya Parc Digital Services — delivery skills for strategy, backlog, tasks, sprint planning, and validation, plus operational skills for specs, stakeholder comms, research, competitive analysis, metrics, and brainstorming. Works in Cursor and Claude Code; standalone with repo context, richer when MCP connectors are connected.

## Installation

Install from this marketplace in Cursor Settings → Plugins, or add the plugin path in Claude Code.

## Skills overview

Each skill produces one clear artefact (markdown file or structured report), except **product-brainstorming** which is a conversation. Invoke with mode first where applicable: `/product write`, `/backlog write`, `/sprint plan 3`.

| Stage | Key outcome(s) | Skills |
| ----- | -------------- | ------ |
| Strategy | _Why? Who? What?_ | **product**, **roadmap** |
| Discovery | _Ready for development_ | **backlog**, **tasks**, **write-spec** |
| Delivery | _Definition of done_ | **sprint**, **validate** |
| Comms & insight | _Inform decisions_ | **stakeholder-update**, **synthesize-research**, **competitive-brief**, **metrics-review** |
| Exploration | _Think before you spec_ | **product-brainstorming** |

## Where files live in your project

Default layout the skills expect (override paths in your prompt if your repo differs):

```text
docs/
├── product/
│   ├── product.md
│   ├── roadmap.md
│   └── backlog.md
└── work/
    ├── {epic}/
    │   ├── design.md
    │   └── tasks.md
    └── sprint-{id}/
        ├── plan.md
        └── retrospective.md
```

**Epic slug `{epic}`** — kebab-case from the epic title or short title, at most two words (`Checkout Foundation` → `checkout-foundation`). Epic IDs like `CHK01` stay in the backlog table; resolve the slug from that row when invoking skills.

Full path and boundary rules: [delivery conventions](skills/references/delivery-conventions.md).

## Skill catalogue

### Strategy

| Skill | Modes | Description | Artefact |
| ----- | ----- | ----------- | -------- |
| **product** | write, review, refine | Product strategy doc (_why_, _who_, _what_) | `docs/product/product.md` |
| **roadmap** | write, review, refine | Outcome-based phases with exit criteria | `docs/product/roadmap.md` |

### Discovery

| Skill | Modes | Description | Artefact |
| ----- | ----- | ----------- | -------- |
| **backlog** | write, review, refine | Epic breakdown, Now-phase scope, work paths | `docs/product/backlog.md` |
| **tasks** | write, review, refine | Task breakdown with Gherkin AC for one epic | `docs/work/{epic}/tasks.md` |
| **write-spec** | — | Feature spec or PRD from a problem statement | feature spec |

### Delivery

| Skill | Modes | Description | Artefact |
| ----- | ----- | ----------- | -------- |
| **sprint** | plan, retrospective | Sprint plan or retrospective | `docs/work/sprint-{id}/plan.md` or `retrospective.md` |
| **validate** | — | Epic completion sign-off vs AC and roadmap gates | validation report |

### Comms & insight

| Skill | Modes | Description | Artefact |
| ----- | ----- | ----------- | -------- |
| **stakeholder-update** | — | Status update tailored to audience and cadence | stakeholder update |
| **synthesize-research** | — | Themes and insights from interviews, surveys, tickets | research synthesis |
| **competitive-brief** | — | Competitive analysis with strategic implications | competitive brief |
| **metrics-review** | — | Metrics review with trends and recommended actions | metrics report |

### Exploration

| Skill | Modes | Description | Artefact |
| ----- | ----- | ----------- | -------- |
| **product-brainstorming** | — | Sparring partner for ideas and assumptions | conversation |

### Utility

| Skill | Modes | Description | Artefact |
| ----- | ----- | ----------- | -------- |
| **skills-index** | — | Route vague requests to the right skill | skill recommendation |

## Typical flow

```text
product → roadmap → backlog
     ↓
design → tasks (design in engineering plugin)
     ↓
implement → code-review → validate
     ↓
sprint (ongoing)     stakeholder-update / metrics-review (as needed)
```

Architecture and implementation skills (**solution**, **adr**, **design**, **implement**, **code-review**, **create-mr**, **docs**, **debug**, **tech-debt**) live in the **engineering** practice plugin when installed. The [delivery conventions](skills/references/delivery-conventions.md) file documents boundaries for all skills.

## Example workflows

### Write product strategy

```
/product write --stage pitch
```

Produces a Shape Up pitch at `docs/product/product.md`.

### Break down an epic

```
/tasks write checkout-foundation
```

Reads `docs/work/checkout-foundation/design.md` and produces Gherkin acceptance criteria in `tasks.md`.

### Plan a sprint

```
/sprint plan 3
```

Creates `docs/work/sprint-3/plan.md` from backlog and task status.

### Write a feature spec

```
/write-spec SSO support for enterprise customers
```

Structured PRD with user stories, requirements, and success metrics.

### Brainstorm before speccing

```
/product-brainstorming Should we add AI-powered search?
```

Conversation-first exploration; follow up with **write-spec** or **product** when ready.

## Standalone + supercharged

Every skill works without integrations:

| What you can do | Standalone | Supercharged with |
| ----------------- | ---------- | ------------------- |
| Product / roadmap / backlog | Paste or describe context | Knowledge base (prior docs) |
| Tasks / validate | Read local `docs/` tree | Project tracker (ticket status) |
| Stakeholder update | Describe progress in chat | Chat, project tracker, knowledge base |
| Research synthesis | Paste interview notes | User feedback, meeting transcription |
| Competitive brief | Describe competitors | Competitive intelligence, knowledge base |
| Metrics review | Paste numbers or describe trends | Product analytics |
| Brainstorm | Think out loud in chat | Analytics, project tracker, knowledge base |

## MCP integrations

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](CONNECTORS.md).

This plugin ships a bundled `.mcp.json` with common SaaS connectors. You can also install standalone connector plugins from `plugins/connectors/` in this repo (GitHub, GitLab, Vercel, Linear, Figma, and others).

| Category | Examples | What it enables |
| -------- | -------- | --------------- |
| **Project tracker** | Linear, Asana, Jira | Backlog status, sprint data, assignments |
| **Chat** | Slack | Team discussions, stakeholder threads |
| **Knowledge base** | Notion, Confluence | Specs, research, meeting notes |
| **Design** | Figma | Design context for specs and tasks |
| **Product analytics** | Amplitude, Pendo | Usage data, metrics, behavioral analysis |
| **User feedback** | Intercom | Support tickets, feature requests |
| **Meeting transcription** | Fireflies | Interview and meeting notes |
| **Competitive intelligence** | Similarweb | Market and competitor data |

See [CONNECTORS.md](CONNECTORS.md) for placeholder categories and supported integrations.

## License

MIT — (c) Carinya Parc Pty Ltd.
