# Engineering Plugin

Engineering practice for Carinya Parc Digital Services — delivery skills for architecture, epic design, implementation, review, and shipping, plus operational skills for debugging and technical debt. Works in Cursor and Claude Code; standalone with repo context, richer when MCP connectors are connected.

## Installation

Install from this marketplace in Cursor Settings → Plugins, or add the plugin path in Claude Code.

## Skills overview

Each skill produces one clear artefact (markdown file, code change, or structured report). Invoke with mode first where applicable: `/design write checkout-foundation`, `/code-review fix`.

| Stage | Key outcome(s) | Skills |
| ----- | -------------- | ------ |
| Architecture | _How? Structure? Principles?_ | **solution**, **adr** |
| Discovery | _Ready for development_ | **design** |
| Delivery | _Definition of done_ | **implement**, **code-review**, **final-code-review**, **create-mr** |
| QA | _Validated against AC_ | **deploy-qa**, **run-automated-suite**, **exploratory-pass**, **document-defects** |
| Refine | _What did we learn?_ | **docs** |
| Operations | _Keep the system healthy_ | **debug**, **tech-debt** |

## Where files live in your project

Default layout the skills expect (override paths in your prompt if your repo differs):

```text
docs/
├── product/
│   ├── product.md
│   ├── roadmap.md
│   └── backlog.md
├── architecture/
│   ├── solution.md
│   └── decisions/
│       ├── register.md
│       └── ADR-NNNN-{title}.md
└── work/
    └── {epic}/
        ├── design.md
        ├── tasks.md
        └── refine-session.md
```

**Epic slug `{epic}`** — kebab-case from the epic title or short title, at most two words (`Checkout Foundation` → `checkout-foundation`). Epic IDs like `CHK01` stay in the backlog table; resolve the slug from that row when invoking skills.

Full path and boundary rules: [delivery conventions](skills/references/delivery-conventions.md).

## Skill catalogue

### Architecture

| Skill | Modes | Description | Artefact |
| ----- | ----- | ----------- | -------- |
| **solution** | write, review, refine | Stub or full arc42-lite `solution.md` | `docs/architecture/solution.md` |
| **adr** | plan, write, review | Proposals in `register.md`; accepted decisions as `ADR-NNNN-{title}.md` | `register.md`, `ADR-NNNN.md` |

### Discovery

| Skill | Modes | Description | Artefact |
| ----- | ----- | ----------- | -------- |
| **design** | write, review | `docs/work/{epic}/design.md` (walking-skeleton or TDD) | `docs/work/{epic}/design.md` |

### Delivery

| Skill | Modes | Description | Artefact |
| ----- | ----- | ----------- | -------- |
| **implement** | — | Implement a task against approved design and tasks | code |
| **code-review** | review, fix | Review a branch or PR; **fix** addresses findings without behaviour changes | code review / code |
| **final-code-review** | — | Final gate on open MR: architecture, security, AC coverage | final review report |
| **create-mr** | run | Merge request description from the branch | MR / PR |

### Refine

| Skill | Modes | Description | Artefact |
| ----- | ----- | ----------- | -------- |
| **docs** | review, refine | Pre-sprint alignment or sprint-end doc pass on product, solution, and epic design | review / `docs/work/{epic}/refine-session.md` |

### Operations

| Skill | Modes | Description | Artefact |
| ----- | ----- | ----------- | -------- |
| **debug** | run | Reproduce, isolate, diagnose, and fix bugs | debug report |
| **tech-debt** | run | Identify, categorize, and prioritize technical debt | prioritized remediation plan |

### QA

| Skill | Modes | Description | Artefact |
| ----- | ----- | ----------- | -------- |
| **deploy-qa** | — | Checkout branch and prepare QA workspace | deploy report |
| **run-automated-suite** | — | Run project automated test command | test report |
| **exploratory-pass** | — | AC-driven exploratory validation | AC checklist / defects |
| **document-defects** | — | Structure reproducible defect reports | defect report |

## Typical flow

```text
solution → adr (optional)
     ↓
design → tasks (in agency-core or sibling plugin)
     ↓
implement → code-review → code-review fix → create-mr
     ↓
docs (ongoing)     debug / tech-debt (as needed)
```

Planning skills (**product**, **backlog**, **tasks**, **validate**, **sprint**) live in sibling practice plugins when installed. The [delivery conventions](skills/references/delivery-conventions.md) file documents boundaries for all skills.

## Example workflows

### Implement a task

```
/implement CHK01-01
```

Reads `docs/work/{epic}/design.md` and `tasks.md`, implements with tests, runs the project validation suite.

### Review before merge

```
/code-review
```

Reviews the branch diff against design scope and Gherkin acceptance criteria. Spawns sub-agents for large diffs.

### Debug a production issue

```
/debug Users are getting 500 errors on checkout
```

Structured reproduce → isolate → diagnose → fix workflow. Pulls logs and recent commits when connectors are available.

### Technical debt audit

```
/tech-debt auth service
```

Prioritized remediation plan scored by impact, risk, and effort.

## Standalone + supercharged

Every skill works without integrations:

| What you can do | Standalone | Supercharged with |
| ----------------- | ---------- | ------------------- |
| Implement / review | Paste design and tasks paths | Source control (PR diffs, branch status) |
| Create MR | Describe branch changes | Source control (auto-fill from commits) |
| Debug | Describe error and steps | Monitoring (logs, metrics), source control |
| ADR / solution / design | Describe system in chat | Knowledge base (prior ADRs, runbooks) |
| Tech debt | Walk the codebase | Project tracker (link remediation tickets) |

## MCP integrations

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](CONNECTORS.md).

This plugin ships a bundled `.mcp.json` with common SaaS connectors. You can also install standalone connector plugins from `connectors/` in this repo (GitHub, GitLab, Vercel, Linear, Playwright, and others).

| Category | Examples | What it enables |
| -------- | -------- | --------------- |
| **Source control** | GitHub, GitLab | PR diffs, commit history, branch status |
| **Project tracker** | Linear, Jira, Asana | Ticket status, sprint data, assignments |
| **Monitoring** | Datadog | Logs, metrics, alerts |
| **Incident management** | PagerDuty | On-call schedules, incident tracking |
| **Chat** | Slack | Team discussions, incident channels |
| **Knowledge base** | Notion, Confluence | ADRs, runbooks, onboarding docs |

See [CONNECTORS.md](CONNECTORS.md) for placeholder categories and supported integrations.

## Bundled with agents

After editing skills here, run from the repo root:

```bash
python3 scripts/sync-agent-skills.py
python3 scripts/validate.py
```

Bundled copies propagate to agents under `agents/` that use the same skill names:

| Agent | Bundled skills from this practice |
| ----- | --------------------------------- |
| **frontend-engineer** | `implement`, `code-review`, `create-mr` |
| **senior-frontend-engineer** | `code-review`, `design` |
| **principal-frontend-engineer** | `final-code-review`, `code-review`, `design` (+ `validate` from product-management) |
| **qa-engineer** | `deploy-qa`, `run-automated-suite`, `exploratory-pass`, `document-defects` |
| **principal-architect** | `solution`, `adr`, `design`, `docs` |

## License

MIT — (c) Carinya Parc Pty Ltd.
