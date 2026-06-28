# AGENCY03 — Repo-Local Tooling Migration

**Status:** Done (2026-06-28)

## Shipped

| Deliverable | Location |
| ----------- | -------- |
| Repo-local maintainer layout | `.agents/` |
| Live eval sessions | `.agents/skills/plugin-eval/SKILL.md` |
| Skill design review | `.agents/skills/skills-qa/SKILL.md` |
| Agency Skill Design Framework | `.agents/references/agency-skill-design-framework.md` |
| Structural validation | `scripts/validate.py` |
| Marketplace clean | `agency-builder-hub` removed from both marketplace manifests |
| Bundled copy citations | validate skill + contributor docs point at `.agents/` paths |

## Removed

- `agency-builder-hub` marketplace plugin
- `.agents/agents/eval-grader.md` — superseded by **plugin-eval**

## Related work

Plugin-eval design and implementation: [`.crew/work/plugin-eval/`](../plugin-eval/)
