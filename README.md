# Digital Agency by Carinya Digital Services

Reference agents, skills, and data connections for a full-service digital agency workflows - digital strategy & growth, creative & content, web development & technical, and operations.

Each agent plugin is designed to be provider-agnostic: they can be deployed behind your own workflow orchestration engine as a Claude (Code, Cowork, Managed Agent), or Cursor (IDE, Cloud Agent) - you choose where it runs.

> [!IMPORTANT]
> Like any workforce, these agents require oversight and governance. They draft work products for review by qualified professionals. You are responsible for verifying outputs and for compliance with the laws and regulations that apply to your business.

What's included

- **[Agents](#agents)** — named, end-to-end workflow agents (Frontend Engineer, …). Each ships as a plugin **and** as a [Managed Agent template](./managed-agents) you deploy via `/v1/agents`.
- **[Functional plugins](#functional-plugins)** — the underlying skills, commands, and data connectors, bundled by vertical. Install these on their own if you just want to access the skills and connectors without a full agent.

## Agents

Each agent is named for the workflow it runs. They're starting points: install the ones that match your work, then tune the prompts, skills, and connectors to how your firm does it.

Each agent plugin is **self-contained** — it bundles the skills it uses, so installing the agent is all you need.

| Function | Agent | What it does |
|---|---|---|
| **Engineering** | **[Frontend Engineer](./plugins/agents/frontend-engineer)** | Builds flexible, performance sites and components, using modern web frameworks. |

For Managed Agent deployment — `agent.yaml`, leaf-worker subagents, steering-event examples, and per-agent security notes — see **[managed-agents/](./managed-agents)**.

## Repository Layout

```
plugins/
  agents/              # Named agents — one self-contained plugin each
  functions/           # Skill + command bundles by vertical, plus MCP connectors
managed-agents/        # Managed Agent cookbooks — one dir per agent
scripts/               # deploy-managed-agent.sh · check.py · validate.py · orchestrate.py · sync-agent-skills.py
```

## Getting Started

### Cowork

In Cowork, open **Settings → Plugins → Add plugin** and either:

- **Paste this repo URL** — `https://github.com/carinyaparc/digital-agency` — then pick the agents and functions you want from the marketplace list, or
- **Upload a zip** — zip any directory under `plugins/` (e.g. `plugins/agents/frontend-engineer/`) and drop it in.

### Claude Managed Agents

Coming soon.

### Cursor

In Cursor, open **Settings → Plugins → Add plugin** and either:

- **Paste this repo URL** — `https://github.com/carinyaparc/digital-agency` — then pick the agents and functions you want from the marketplace list, or
- **Upload a zip** — zip any directory under `plugins/` (e.g. `plugins/agents/frontend-engineer/`) and drop it in.

### Cursor Cloud Agents

Coming soon.

## How It Fits Together

| | What it is | Where it lives |
|---|---|---|
| **Agents** | Self-contained plugins that own a workflow end to end — system prompt plus the skills it uses. Cowork and the Managed Agent wrapper both reference the same directory. | `plugins/agents/<slug>/` |
| **Skills** | Domain expertise, conventions, and step-by-step methods Claude draws on automatically when relevant. Authored once in the verticals; each agent bundles a synced copy of the ones it needs. | `plugins/functions/<function>/skills/` (source) · `plugins/agents/<slug>/skills/` (bundled) |
| **Commands** | Slash actions you trigger explicitly (`/implement`). | `plugins/functions/<function>/commands/` |
| **Connectors** | [MCP servers](https://modelcontextprotocol.io/) that wire agents to your data — source code, code reviews, hosting, observability, analytics. | `plugins/functions/agency-core/.mcp.json` |
| **Managed-agent wrappers** | `agent.yaml` + depth-1 subagents + steering examples for headless deployment. | `managed-agents/<slug>/` |

Everything is file-based — markdown and JSON, no build step.

## Functional Plugins

Start with **agency-core** — it carries the shared skills and all data connectors. Add verticals for the workflows you need.

| Plugin | What it adds |
|---|---|
| **[agency-core](./plugins/functions/agency-core)** | Core digital agency skills (coming soon). Shared data connectors. |
| **[engineering](./plugins/functions/engineering)** | Feature delivery, coding, component development, code review. |

## MCP Integrations

All connectors are centralized in the `agency-core` core plugin and shared across the rest.

| Provider | Type | URL / package |
|---|---|---|
| [GitHub](https://github.com/) | HTTP | `https://api.githubcopilot.com/mcp/` |
| [Vercel](https://vercel.com/) | HTTP | `https://mcp.vercel.com` |
| [Figma](https://www.figma.com/) | HTTP | `https://mcp.figma.com/mcp` |
| [Linear](https://linear.app/) | HTTP | `https://mcp.linear.app/mcp` |
| [Playwright](https://playwright.dev/) | npx | `@playwright/mcp@latest` |
| [Context7](https://context7.com/) | npx | `@upstash/context7-mcp` |
| [Next.js DevTools](https://nextjs.org/) | npx | `next-devtools-mcp@latest` |

> MCP access may require authentication, subscription, or an API key from the provider.

## Making It Yours

These are reference templates — they get better when you tune them to how your firm works.

- **Swap connectors** — point `.mcp.json` at your data providers and internal systems.
- **Add firm context** — drop your terminology, processes, and formatting standards into skill files.
- **Bring your brand voice** — `/brand-voice` teaches agents your brand voice, writing style and structure.
- **Adjust agent scope** — edit `agents/<slug>.md` to match how your team actually runs the workflow.
- **Add your own** — copy the structure for workflows we haven't covered.

## Skill & Command Reference

<details>
<summary><b>agency-core</b> — coming soon</summary>

| Skill | Modes | Description | Artefact |
| ----- | ----- | ----------- | -------- |

</details>

<details>
<summary><b>engineering</b> — implement, code review, create merge request</summary>

| Skill | Modes | Description | Artefact |
| ----- | ----- | ----------- | -------- |
| **implement** | — | Implement a task against approved design and tasks | code |
| **code-review** | review | Review a branch or PR against design.md and tasks.md acceptance criteria | code review |
| **code-review fix** | fix | Address review findings without behaviour changes | code |
| **create-mr** | run | Merge request description from the branch | MR / PR |

</details>

## Contributing

Everything here is markdown and YAML. Fork, edit, PR. For new content:

- New skill → add it under `plugins/functions/<function>/skills/`, then run `python3 scripts/sync-agent-skills.py` to propagate to any agent that bundles it.
- New agent → `plugins/agents/<slug>/` (with `agents/<slug>.md` + `skills/`) and a matching `managed-agents/<slug>/`.
- Run `python3 scripts/check.py` before pushing — it lints every manifest, verifies all cross-file references resolve, and fails if any bundled skill has drifted from its vertical source.

## License

[MIT](./LICENSE)

(c) 2026 Carinya Parc Pty Ltd.
