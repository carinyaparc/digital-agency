# Changelog

All notable changes to this project are documented here. Version numbers match
Git tags and the `version` field in `.cursor-plugin/plugin.json` and
`.claude-plugin/plugin.json`.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Changed

- **AGENCY03 complete** — repo-local maintainer tooling in `.agents/` (`plugin-eval`, `skills-qa`, skill-design framework); `agency-builder-hub` removed from marketplace
- **plugin-eval** replaces **eval-grader** — live eval sessions via `.agents/skills/plugin-eval/SKILL.md`
- Skill plugins moved from `plugins/skills/` to repo root `skills/`
- MCP connector plugins moved from `plugins/connectors/` to repo root `connectors/`

### Added

- **`scripts/validate.py`** — structural validation for marketplace manifests, plugin.json, MCP connectors, SKILL.md frontmatter, markdown cross-references, bundled-skill drift, and evals schema (`--format json`, `--strict`, `--skip-drift`)
- **`.agents/`** local maintainer tooling — `plugin-eval` skill, `skills-qa` skill, and Agency Skill Design Framework in `references/`
- Connector plugins under `plugins/connectors/` — GitHub, GitLab, Vercel, Figma, Linear, Playwright, Context7, Next.js DevTools
- Agent plugin **senior-frontend-engineer** — peer code reviewer for React/Next.js UI; bundles `code-review` and `design` from the engineering practice
- Agent plugin **product-manager** — full product delivery lifecycle; bundles all 13 skills from the product-management practice
- Agent plugin **principal-frontend-engineer** — final technical gate on open PRs/MRs; bundles `final-code-review`, `code-review`, `design`, `validate`
- Engineering skill **final-code-review** — post-MR architecture and AC gate (adapted from delivery-review crew)
- Agent plugin **qa-engineer** — QA validation after CI; bundles `deploy-qa`, `run-automated-suite`, `exploratory-pass`, `document-defects`
- Engineering QA skills — `deploy-qa`, `run-automated-suite`, `exploratory-pass`, `document-defects` (adapted from delivery-qa crew)
- Agent plugin **delivery-lead** — cross-cutting delivery orchestration; bundles sprint, backlog, tasks, validate, stakeholder-update, metrics-review, skills-index
- Agent plugin **principal-architect** — system architecture track; bundles `solution`, `adr`, `design`, `docs`

### Removed

- **agency-builder-hub** marketplace plugin — maintainer tooling moved to `.agents/`
- **eval-grader** agent — replaced by **plugin-eval** skill
- `agency-core` practice plugin — MCP connectors moved to `plugins/connectors/`

## [0.1.0] - 2026-06-21

Initial release of Carinya Parc Digital Agency

## Added

- Functional plugins: `agency-core`, `engineering`
- Agent plugins: `frontend-engineer`
