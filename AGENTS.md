# Digital Agency Plugins

Cowork and Cursor plugins and Claude Managed Agent templates for digital agency workflows. Each named agent ships two ways from one source.

## Repository Structure

```
├── agents/                          # shared agents used across plugins (e.g. eval-grader)
├── plugins/
│   ├── agents/                      # named agents — one self-contained plugin each
│   │   └── <slug>/
│   │       ├── .claude-plugin/plugin.json
│   │       ├── .cursor-plugin/plugin.json
│   │       ├── agents/<slug>.md     #   ← canonical system prompt (one source, two wrappers)
│   │       └── skills/              #   ← bundled copies, synced from skills/
│   ├── connectors/                  #   MCP connector plugins — one provider each
│   │   └── <slug>/
│   │       ├── .claude-plugin/plugin.json
│   │       ├── .cursor-plugin/plugin.json
│   │       └── .mcp.json            #   ← canonical MCP definition
│   └── skills/                      #   skill plugins — skill sources, commands
│       └── <discipline>/
│           ├── .claude-plugin/plugin.json
│           ├── .cursor-plugin/plugin.json
│           ├── commands/
│           └── skills/
│               └── <name>/
│                   ├── SKILL.md
│                   ├── prompts/
│                   ├── agents/      #   sub-agents for this skill
│                   ├── evals/       #   evals.json + trigger-queries.json
│                   └── scripts/     #   optional helper scripts
├── managed-agents/                  #   CMA cookbooks (coming soon) — one dir per named agent
│   └── <slug>/
│       ├── agent.yaml               #   system + skills → ../../plugins/agents/<slug>/...
│       ├── subagents/*.yaml         #   depth-1 leaf workers
│       ├── steering-examples.json
│       └── README.md                #   security tier + handoff notes
└── scripts/                         # sync-agent-skills.py (+ check.py, validate.py, orchestrate.py, deploy-managed-agent.sh — coming soon)
```

Run `python3 scripts/sync-agent-skills.py` after editing a skill under `plugins/skills/` — it propagates bundled copies into every agent under `plugins/agents/` that uses that skill. **Edit skills in `plugins/skills/`**, not in agent bundles.

`check.py` (coming soon) will lint every manifest, verify all cross-file references resolve, and fail if any `agents/<slug>/skills/` copy has drifted from its `plugins/skills/` source. A pre-commit hook and `version-bump` GitHub Action (coming soon) will patch-bump each plugin's `plugin.json` `version` so a branch ends up exactly one patch ahead of `main`.

## Agents (current roster)

| Slug | Practice | Bundled skills | Status |
| ---- | -------- | -------------- | ------ |
| `frontend-engineer` | Engineering | `implement`, `code-review`, `create-mr`, `brand-guide`, `component-scaffold` (agent-local) | Shipped; not yet operationally proven |
| `senior-frontend-engineer` | Engineering | `code-review`, `design` | Shipped; not yet operationally proven |
| `product-manager` | Product | All 13 product-management skills (`product`, `roadmap`, `backlog`, `tasks`, `sprint`, `validate`, `write-spec`, `stakeholder-update`, `synthesize-research`, `competitive-brief`, `metrics-review`, `product-brainstorming`, `skills-index`) | Shipped; not yet operationally proven |

Each agent lives under `plugins/agents/<slug>/` with a canonical system prompt at `agents/<slug>.md`, bundled skills at `skills/`, and role-specific MCP in `.mcp.json`. Register new agents in both marketplace manifests.

## Key Files

- `.claude-plugin/marketplace.json` / `.cursor-plugin/marketplace.json`: Marketplace manifests — register all plugins with source paths
- `plugin.json`: Plugin metadata — name, description, version, and component discovery settings
- `commands/*.md`: Slash commands invoked as `/plugin:command-name`
- `skills/*/SKILL.md`: Detailed knowledge and workflows for specific tasks
- `plugins/connectors/<slug>/.mcp.json`: Canonical MCP connector definitions (GitHub, GitLab, Vercel, Figma, Linear, Playwright, Context7, Next.js DevTools)
- `*.local.md`: User-specific configuration (gitignored)

## Development Workflow

1. Edit markdown files directly — changes take effect immediately
2. Test commands with `/plugin:command-name` syntax (Cowork) or install via Cursor Settings → Plugins
3. Skills are invoked automatically when their trigger conditions match
