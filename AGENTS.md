# Digital Agency Plugins

Cowork and Cursor plugins and Claude Managed Agent templates for digital agency workflows. Each named agent ships two ways from one source.

## Repository Structure

```
├── plugins/
│   ├── agents/                      # named agents — one self-contained plugin each
│   │   └── <slug>/
│   │       ├── .claude-plugin/plugin.json
│   │       ├── .cursor-plugin/plugin.json
│   │       ├── agents/<slug>.md     #   ← canonical system prompt (one source, two wrappers)
│   │       └── skills/              #   ← bundled copies, synced from functions/
│   └── functions/                   #   functional plugins — skill sources, commands, MCPs
│       └── <function>/
│           ├── .claude-plugin/plugin.json
│           ├── .cursor-plugin/plugin.json
│           ├── commands/
│           ├── skills/
│           └── .mcp.json            #   agency-core only — shared connectors
├── managed-agents/                  #   CMA cookbooks (coming soon) — one dir per named agent
│   └── <slug>/
│       ├── agent.yaml               #   system + skills → ../../plugins/agents/<slug>/...
│       ├── subagents/*.yaml         #   depth-1 leaf workers
│       ├── steering-examples.json
│       └── README.md                #   security tier + handoff notes
└── scripts/                         # sync-agent-skills.py (+ check.py, validate.py, orchestrate.py, deploy-managed-agent.sh — coming soon)
```

Run `python3 scripts/sync-agent-skills.py` after editing a skill under `plugins/functions/` — it propagates bundled copies into every agent under `plugins/agents/` that uses that skill. **Edit skills in `functions/`**, not in agent bundles.

`check.py` (coming soon) will lint every manifest, verify all cross-file references resolve, and fail if any `agents/<slug>/skills/` copy has drifted from its `functions/` source. A pre-commit hook and `version-bump` GitHub Action (coming soon) will patch-bump each plugin's `plugin.json` `version` so a branch ends up exactly one patch ahead of `main`.

## Key Files

- `.claude-plugin/marketplace.json` / `.cursor-plugin/marketplace.json`: Marketplace manifests — register all plugins with source paths
- `plugin.json`: Plugin metadata — name, description, version, and component discovery settings
- `commands/*.md`: Slash commands invoked as `/plugin:command-name`
- `skills/*/SKILL.md`: Detailed knowledge and workflows for specific tasks
- `*.local.md`: User-specific configuration (gitignored)
- `plugins/functions/agency-core/.mcp.json`: Shared MCP connectors (GitHub, Vercel, Figma, Linear, Playwright, Context7, Next.js DevTools)

## Development Workflow

1. Edit markdown files directly — changes take effect immediately
2. Test commands with `/plugin:command-name` syntax (Cowork) or install via Cursor Settings → Plugins
3. Skills are invoked automatically when their trigger conditions match
