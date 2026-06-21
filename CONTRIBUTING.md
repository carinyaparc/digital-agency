# Contributing to Digital Agency

Everything in this repo is markdown and JSON — no build step. Fork, edit, open a PR.

## Layout

```text
plugins/
  agents/<slug>/              # named agents — self-contained plugins
    agents/<slug>.md          # system prompt (canonical)
    skills/                   # bundled copies — do not edit directly
    .claude-plugin/plugin.json
    .cursor-plugin/plugin.json
  practices/<practice>/       # skill and command sources
    skills/<name>/SKILL.md
    commands/
    .mcp.json                 # agency-core only — shared MCP connectors

managed-agents/<slug>/        # Managed Agent cookbooks (agent.yaml, subagents, …)

.cursor-plugin/marketplace.json
.claude-plugin/marketplace.json
```

**Source of truth:** edit skills under `plugins/practices/`, not under `plugins/agents/`. Agent plugins bundle synced copies so they stay installable on their own.

## Changing a skill

1. Edit `plugins/practices/<practice>/skills/<name>/`.
2. Update the skill `description` in frontmatter when routing or scope changes.
3. Run sync to propagate into every agent that bundles it:

   ```bash
   python3 scripts/sync-agent-skills.py
   ```

4. Test in Cowork or Cursor — install the practice plugin or an agent that bundles the skill.

## Adding a skill

1. Create `plugins/practices/<practice>/skills/<name>/SKILL.md` (and optional `prompts/`, `agents/`, etc.).
2. Register it in the practice plugin’s `plugin.json` if needed.
3. Add a bundled copy to any agent that should use it under `plugins/agents/<slug>/skills/<name>/`.
4. Run `python3 scripts/sync-agent-skills.py`.

## Adding or changing an agent

1. Add `plugins/agents/<slug>/` with:
   - `agents/<slug>.md` — system prompt
   - `skills/` — bundled skills (synced from practices)
   - `.claude-plugin/plugin.json` and `.cursor-plugin/plugin.json`
2. Register the plugin in `.cursor-plugin/marketplace.json` and `.claude-plugin/marketplace.json`.
3. Add a matching `managed-agents/<slug>/` when Managed Agent deployment is in scope.

Follow existing agents (e.g. `plugins/agents/frontend-engineer/`) for structure and naming.

## Commands and connectors

- **Commands** — slash actions live in `plugins/practices/<practice>/commands/`. Invoked as `/plugin:command-name` in Cowork.
- **MCP connectors** — shared in `plugins/practices/agency-core/.mcp.json`. Point entries at your providers; do not commit secrets or API keys.

## Pull requests

- Run `python3 scripts/sync-agent-skills.py` after any skill change under `plugins/practices/`.
- Register new plugins in both marketplace manifests.
- Describe what workflow or agent behaviour changed and how you tested it (Cowork, Cursor, or local install).
- Keep changes focused — one skill, agent, or practice per PR when possible.

## Local config

User-specific overrides belong in `*.local.md` files (gitignored). Do not commit credentials or client data.
