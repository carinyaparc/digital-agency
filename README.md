# Digital Agency by Carinya Parc

Reference agents, skills, and data connections for a full-service digital agency workflows - digital strategy & growth, creative & content, web development & technical, and operations.

Each agent plugin is designed to be provider-agnostic: they can be deployed behind your own workflow orchestration engine as a Claude (Code, Cowork, Managed Agent), or Cursor (IDE, Cloud Agent) - you choose where it runs.

> [!IMPORTANT]
> Like any workforce, these agents require oversight and governance. They draft work products for review by qualified professionals. You are responsible for verifying outputs and for compliance with the laws and regulations that apply to your business.

What's included

- **[Agents](#agents)** — named, end-to-end workflow agents (Frontend Engineer, …). Each ships as a plugin **and** as a [Managed Agents](./managed-agents) you deploy via `/v1/agents`.
- **[Skill plugins](#skill-plugins)** — the underlying skills and commands, bundled by discipline. Install these on their own if you just want the skills without a full agent.
- **[Connectors](#mcp-integrations)** — MCP data connectors, one provider per plugin. Install the ones your workflows need alongside agents and practices.

## Agents

Each agent is named for the workflow it runs. They're starting points: install the ones that match your work, then tune the prompts, skills, and connectors to how your firm does it.

Each agent plugin is **self-contained** — it bundles the skills it uses, so installing the agent is all you need.

| Practice | Agent | What it does |
|---|---|---|
| **Engineering** | **[Frontend Engineer](./plugins/agents/frontend-engineer)** | Builds flexible, performance sites and components, using modern web frameworks. |

For Managed Agent deployment — `agent.yaml`, leaf-worker subagents, steering-event examples, and per-agent security notes — see **[managed-agents/](./managed-agents)**.

## Repository Layout

```
plugins/
  agents/              # Named agents — one self-contained plugin each
  connectors/          # MCP connector plugins — one provider each
  skills/              # Skill + command bundles by discipline
managed-agents/        # Managed Agent cookbooks — one dir per agent
scripts/               # deploy-managed-agent.sh · check.py · validate.py · orchestrate.py · sync-agent-skills.py
```

## Getting Started

### Cowork

In Cowork, open **Settings → Plugins → Add plugin** and either:

- **Paste this repo URL** — `https://github.com/carinyaparc/digital-agency` — then pick the agents and skills you want from the marketplace list, or
- **Upload a zip** — zip any directory under `plugins/` (e.g. `plugins/agents/frontend-engineer/`) and drop it in.

### Claude Managed Agents

Coming soon.

### Cursor

In Cursor, open **Settings → Plugins → Add plugin** and either:

- **Paste this repo URL** — `https://github.com/carinyaparc/digital-agency` — then pick the agents and skills you want from the marketplace list, or
- **Upload a zip** — zip any directory under `plugins/` (e.g. `plugins/agents/frontend-engineer/`) and drop it in.

### Cursor Cloud Agents

Coming soon.

## How It Fits Together

| | What it is | Where it lives |
|---|---|---|
| **Agents** | Self-contained plugins that own a workflow end to end — system prompt plus the skills it uses. Cowork and the Managed Agent wrapper both reference the same directory. | `plugins/agents/<slug>/` |
| **Skills** | Domain expertise, conventions, and step-by-step methods Claude draws on automatically when relevant. Authored once per discipline; each agent bundles a synced copy of the ones it needs. | `plugins/skills/<discipline>/skills/` (source) · `plugins/agents/<slug>/skills/` (bundled) |
| **Commands** | Slash actions you trigger explicitly (`/implement`). | `plugins/skills/<discipline>/commands/` |
| **Connectors** | [MCP servers](https://modelcontextprotocol.io/) that wire agents to your data — source code, code reviews, hosting, observability, analytics. | `plugins/connectors/<slug>/.mcp.json` |
| **Managed-agent wrappers** | `agent.yaml` + depth-1 subagents + steering examples for headless deployment. | `managed-agents/<slug>/` |

Everything is file-based — markdown and JSON, no build step.

## Skill Plugins

Install skill plugins for the disciplines you need.

| Plugin | What it adds |
|---|---|
| **[engineering](./plugins/skills/engineering)** | Architecture, epic design, implementation, code review, debugging, and technical debt. |
| **[product-management](./plugins/skills/product-management)** | Product strategy, roadmap, backlog, tasks, sprint planning, validation, specs, stakeholder updates, research, competitive analysis, metrics, and brainstorming. |
| **[brand](./plugins/skills/brand)** | Visual brand guide and brand voice lifecycle — discover, write, review, refine, and enforce on-brand copy. |

## MCP Integrations

Each connector is a standalone plugin under `plugins/connectors/`. Install the providers your stack uses — agents will bundle recommended connectors later.

| Plugin | Provider | Type | URL / package |
|---|---|---|---|
| **[context7](./plugins/connectors/context7)** | [Context7](https://context7.com/) | npx | `@upstash/context7-mcp` |
| **[figma](./plugins/connectors/figma)** | [Figma](https://www.figma.com/) | HTTP | `https://mcp.figma.com/mcp` |
| **[github](./plugins/connectors/github)** | [GitHub](https://github.com/) | HTTP | `https://api.githubcopilot.com/mcp/` |
| **[gitlab](./plugins/connectors/gitlab)** | [GitLab](https://gitlab.com/) | HTTP | `https://gitlab.com/api/v4/mcp` |
| **[vercel](./plugins/connectors/vercel)** | [Vercel](https://vercel.com/) | HTTP | `https://mcp.vercel.com` |
| **[linear](./plugins/connectors/linear)** | [Linear](https://linear.app/) | HTTP | `https://mcp.linear.app/mcp` |
| **[playwright](./plugins/connectors/playwright)** | [Playwright](https://playwright.dev/) | npx | `@playwright/mcp@latest` |
| **[next-devtools](./plugins/connectors/next-devtools)** | [Next.js DevTools](https://nextjs.org/) | npx | `next-devtools-mcp@latest` |

> MCP access may require authentication, subscription, or an API key from the provider.

## Making It Yours

These are reference templates — they get better when you tune them to how your firm works.

- **Swap connectors** — fork a connector under `plugins/connectors/` or point `.mcp.json` at your data providers and internal systems.
- **Add firm context** — drop your terminology, processes, and formatting standards into skill files.
- **Bring your brand voice** — `/brand-voice write` and `/brand-voice enforce` teach agents your voice; `/brand-guide write` for visual identity in `docs/brand/`.
- **Adjust agent scope** — edit `agents/<slug>.md` to match how your team actually runs the workflow.
- **Add your own** — copy the structure for workflows we haven't covered.

## Skill & Command Reference

<details>
<summary><b>engineering</b> — solution, adr, design, implement, code review, docs, debug, tech-debt</summary>

See [engineering README](./plugins/skills/engineering/README.md) for full detail.

| Skill | Modes | Description | Artefact |
| ----- | ----- | ----------- | -------- |
| **solution** | write, review, refine | System architecture (stub or full) | `docs/architecture/solution.md` |
| **adr** | plan, write, review | Architecture decision register and ADR files | `register.md`, `ADR-NNNN.md` |
| **design** | write, review | Epic-level technical design | `docs/work/{epic}/design.md` |
| **implement** | — | Implement a task against approved design and tasks | code |
| **code-review** | review, fix | Review a branch or PR; fix addresses findings | code review / code |
| **create-mr** | run | Merge request description from the branch | MR / PR |
| **docs** | review, refine | Pre-sprint or sprint-end documentation pass | review / `refine-session.md` |
| **debug** | run | Reproduce, isolate, diagnose, and fix bugs | debug report |
| **tech-debt** | run | Prioritize technical debt remediation | remediation plan |

</details>

<details>
<summary><b>brand</b> — brand-guide, brand-voice</summary>

See [brand README](./plugins/skills/brand/README.md) for full detail.

| Skill | Modes | Description | Artefact |
| ----- | ----- | ----------- | -------- |
| **brand-guide** | write, review, refine | Visual identity — colors, type, logo, UI tokens | `docs/brand/brand-guide.md` |
| **brand-voice** | discover, write, review, refine, enforce | Voice lifecycle and on-brand copy | `docs/brand/brand-voice.md`, `discovery-report.md`, inline content |

</details>

## Contributing

Everything here is markdown and YAML. Fork, edit, PR. For new content:

- New skill → add it under `plugins/skills/<discipline>/skills/`, then run `python3 scripts/sync-agent-skills.py` to propagate to any agent that bundles it.
- New agent → `plugins/agents/<slug>/` (with `agents/<slug>.md` + `skills/`) and a matching `managed-agents/<slug>/`.
- Run `python3 scripts/check.py` before pushing — it lints every manifest, verifies all cross-file references resolve, and fails if any bundled skill has drifted from its vertical source.

## License

[MIT](./LICENSE)

(c) 2026 Carinya Parc Pty Ltd.
