# Changelog

All notable changes to this project are documented here. Version numbers match
Git tags and the `version` field in `.cursor-plugin/plugin.json` and
`.claude-plugin/plugin.json`.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Added

- **agency-builder-hub** plugin at repo root — `eval-grader` agent and `skills-qa` skill; Agency Skill Design Framework in `references/`
- Connector plugins under `plugins/connectors/` — GitHub, GitLab, Vercel, Figma, Linear, Playwright, Context7, Next.js DevTools
- Agent plugin **senior-frontend-engineer** — peer code reviewer for React/Next.js UI; bundles `code-review` and `design` from the engineering practice
- Agent plugin **product-manager** — full product delivery lifecycle; bundles all 13 skills from the product-management practice

### Removed

- Root `agents/` folder — `eval-grader` moved to `agency-builder-hub/agents/`
- `agency-core` practice plugin — MCP connectors moved to `plugins/connectors/`

## [0.1.0] - 2026-06-21

Initial release of Carinya Parc Digital Agency

## Added

- Functional plugins: `agency-core`, `engineering`
- Agent plugins: `frontend-engineer`
