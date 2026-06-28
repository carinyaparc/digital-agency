# Local maintainer tooling

Repo-local agents, skills, and references for building and shipping plugins in
this repository. Not published as a marketplace plugin — use these paths directly
in Cowork, Cursor, or Claude Code when authoring or tuning skills under
`skills/`.

## Tools

| Tool | Path | Purpose |
| --- | --- | --- |
| **plugin-eval** | [`skills/plugin-eval/SKILL.md`](./skills/plugin-eval/SKILL.md) | Live eval sessions — grade `evals/evals.json` assertions with evidence; write coverage report |
| **skills-qa** | [`skills/skills-qa/SKILL.md`](./skills/skills-qa/SKILL.md) | Evaluate a skill against the Agency Skill Design Framework before shipping |
| **validate.py** | [`../scripts/validate.py`](../scripts/validate.py) | Structural repo validation — manifests, cross-refs, bundled-skill drift, evals schema |

Run **plugin-eval** before shipping skill changes, or when assertions pass but
output quality is poor.

Run **skills-qa** by following [`skills/skills-qa/SKILL.md`](./skills/skills-qa/SKILL.md)
with a skill path, `SKILL.md` path, or pasted content.

Run **`python3 scripts/validate.py`** before every PR — see
[`CONTRIBUTING.md`](../CONTRIBUTING.md#validation) for the full check list and flags.

## Framework

The canonical design standard lives at
[`references/agency-skill-design-framework.md`](./references/agency-skill-design-framework.md).
`skills-qa` cites it — keep them in sync when the framework changes.

## Related docs

- Repository layout: [`AGENTS.md`](../AGENTS.md)
- Contributing skills and evals: [`CONTRIBUTING.md`](../CONTRIBUTING.md)
