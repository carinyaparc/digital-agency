# Agency Builder Hub Plugin

Skill quality tooling for the Carinya Digital Services reference. v0 ships
**eval-grader** (grade skill eval runs) and **skills-qa** (evaluate skills
against the Agency Skill Design Framework before shipping).

Future versions will add community skill discovery and install — the same
pattern as [strategy-builder-hub](https://github.com/daddia/claude-for-strategy/tree/main/strategy-builder-hub)
and [legal-builder-hub](https://github.com/anthropics/claude-for-legal/tree/main/legal-builder-hub).

## Who this is for

Maintainers and contributors authoring or tuning skills under `plugins/skills/`
and bundled agent copies. Install this plugin when you run eval batches or
want a structured pre-ship review of a skill's design.

## Commands

| Command | Does |
| --- | --- |
| `/agency-builder-hub:skills-qa [skill path]` | Evaluate a skill against the Agency Skill Design Framework |

## Agents

| Agent | Purpose |
| --- | --- |
| **eval-grader** | PASS/FAIL each assertion in `evals/evals.json` with evidence; critique eval quality |

Invoke eval-grader after a with-skill eval batch, or when assertions pass but
output quality is poor.

## Skills

| Skill | Purpose |
| --- | --- |
| **skills-qa** | Design-quality and trust-surface review before shipping a skill |

## Framework

The canonical design standard lives at
[`references/agency-skill-design-framework.md`](./references/agency-skill-design-framework.md).
`skills-qa` cites it — keep them in sync when the framework changes.

## Related docs

- Repository layout: [`AGENTS.md`](../AGENTS.md)
- Contributing skills and evals: [`CONTRIBUTING.md`](../CONTRIBUTING.md)
