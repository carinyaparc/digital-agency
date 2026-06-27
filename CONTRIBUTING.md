# Contributing to Digital Agency

Everything in this repo is markdown and JSON — no build step. Fork, edit, open a PR.

## Layout

```text
agency-builder-hub/           # skill quality hub — eval-grader, skills-qa

plugins/
  agents/<slug>/              # named agents — self-contained plugins
    agents/<slug>.md          # system prompt (canonical)
    skills/                   # bundled copies — do not edit directly
    .claude-plugin/plugin.json
    .cursor-plugin/plugin.json
  connectors/<slug>/          # MCP connector plugins — one provider each
    .mcp.json                 # canonical MCP definition
    .claude-plugin/plugin.json
    .cursor-plugin/plugin.json
  skills/<discipline>/        # skill and command sources
    skills/<name>/
      SKILL.md
      prompts/
      agents/                 # sub-agents scoped to this skill
      evals/                  # evals.json + trigger-queries.json
      scripts/                # optional helper scripts
    commands/

managed-agents/<slug>/        # Managed Agent cookbooks (agent.yaml, subagents, …)

.cursor-plugin/marketplace.json
.claude-plugin/marketplace.json
```

**Source of truth:** edit skills under `plugins/skills/`, not under `plugins/agents/`. Agent plugins bundle synced copies so they stay installable on their own. Edit MCP connectors under `plugins/connectors/`, not in agent bundles.

## Changing a skill

1. Edit `plugins/skills/<discipline>/skills/<name>/`.
2. Update the skill `description` in frontmatter when routing or scope changes.
3. Run sync to propagate into every agent that bundles it:

   ```bash
   python3 scripts/sync-agent-skills.py
   ```

4. Test in Cowork or Cursor — install the skill plugin or an agent that bundles the skill.

## Adding a skill

1. Create `plugins/skills/<discipline>/skills/<name>/SKILL.md` (and optional `prompts/`, `agents/`, `evals/`, `scripts/`).
2. Add `evals/evals.json` and `evals/trigger-queries.json` to define test cases and routing expectations.
3. Run eval batches and grade with **eval-grader** from [`agency-builder-hub/agents/eval-grader.md`](./agency-builder-hub/agents/eval-grader.md).
4. Run `/agency-builder-hub:skills-qa` on the skill before shipping.
5. Register it in the discipline plugin’s `plugin.json` if needed.
6. Add a bundled copy to any agent that should use it under `plugins/agents/<slug>/skills/<name>/`.
7. Run `python3 scripts/sync-agent-skills.py`.

## Adding or changing an agent

1. Add `plugins/agents/<slug>/` with:
   - `agents/<slug>.md` — system prompt
   - `skills/` — bundled skills (synced from `plugins/skills/`)
   - `.claude-plugin/plugin.json` and `.cursor-plugin/plugin.json`
2. Register the plugin in `.cursor-plugin/marketplace.json` and `.claude-plugin/marketplace.json`.
3. Add a matching `managed-agents/<slug>/` when Managed Agent deployment is in scope.

Follow existing agents (e.g. `plugins/agents/frontend-engineer/`, `plugins/agents/senior-frontend-engineer/`, `plugins/agents/product-manager/`) for structure and naming. See the [Agents roster](../../AGENTS.md#agents-current-roster) in `AGENTS.md`.

## Adding or changing a connector

1. Add `plugins/connectors/<slug>/` with:
   - `.mcp.json` — one MCP server definition
   - `.claude-plugin/plugin.json` and `.cursor-plugin/plugin.json` with `"mcpServers": "./.mcp.json"`
2. Register the plugin in both marketplace manifests.
3. Do not commit secrets or API keys — use env var placeholders where providers require auth.

Follow existing connectors (e.g. `plugins/connectors/github/`) for structure and naming.

## Commands and connectors

- **Commands** — slash actions live in `plugins/skills/<discipline>/commands/`. Invoked as `/plugin:command-name` in Cowork.
- **MCP connectors** — one provider per plugin under `plugins/connectors/<slug>/.mcp.json`. Point entries at your providers; do not commit secrets or API keys.

## Pull requests

- Run `python3 scripts/sync-agent-skills.py` after any skill change under `plugins/skills/`.
- Register new plugins in both marketplace manifests.
- Add or update `evals/evals.json` and `evals/trigger-queries.json` for any new or changed skill; grade with **eval-grader**; run `/agency-builder-hub:skills-qa` before merge.
- Describe what workflow or agent behaviour changed and how you tested it (Cowork, Cursor, or local install).
- Keep changes focused — one skill, agent, discipline, or connector per PR when possible.

## Local config

User-specific overrides belong in `*.local.md` files (gitignored). Do not commit credentials or client data.
