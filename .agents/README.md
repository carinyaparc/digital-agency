# Local maintainer tooling

Repo-local agents, skills, and references for building and shipping plugins in
this repository. Not published as a marketplace plugin — use these paths directly
in Cowork, Cursor, or Claude Code when authoring or tuning skills under
`plugins/skills/`.

## Tools

| Tool | Path | Purpose |
| --- | --- | --- |
| **eval-grader** | [`agents/eval-grader.md`](./agents/eval-grader.md) | PASS/FAIL each assertion in `evals/evals.json` with evidence; critique eval quality |
| **skills-qa** | [`skills/skills-qa/SKILL.md`](./skills/skills-qa/SKILL.md) | Evaluate a skill against the Agency Skill Design Framework before shipping |

Invoke **eval-grader** after a with-skill eval batch, or when assertions pass but
output quality is poor.

Run **skills-qa** by following [`skills/skills-qa/SKILL.md`](./skills/skills-qa/SKILL.md)
with a skill path, `SKILL.md` path, or pasted content.

## Framework

The canonical design standard lives at
[`references/agency-skill-design-framework.md`](./references/agency-skill-design-framework.md).
`skills-qa` cites it — keep them in sync when the framework changes.

## Related docs

- Repository layout: [`AGENTS.md`](../AGENTS.md)
- Contributing skills and evals: [`CONTRIBUTING.md`](../CONTRIBUTING.md)
