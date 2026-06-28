# Connectors

## How tool references work

Plugin files use `~~category` as a placeholder for whatever tool the user connects in that category. For example, `~~source control` might mean GitHub, GitLab, or any other VCS with an MCP server.

Plugins are **tool-agnostic** — they describe workflows in terms of categories (source control, CI/CD, monitoring, etc.) rather than specific products. The `.mcp.json` pre-configures specific MCP servers, but any MCP server in that category works.

Standalone connector plugins in this repo live under `connectors/<slug>/.mcp.json` — install those instead of or alongside the bundled servers below.

## Connectors for this plugin

| Category | Placeholder | Bundled in `.mcp.json` | Also in `connectors/` |
| -------- | ----------- | ---------------------- | ------------------------------ |
| Chat | `~~chat` | Slack | — |
| Source control | `~~source control` | GitHub | GitHub, GitLab |
| Project tracker | `~~project tracker` | Linear, Asana, Atlassian (Jira/Confluence) | Linear |
| Knowledge base | `~~knowledge base` | Notion | — |
| Monitoring | `~~monitoring` | Datadog | — |
| Incident management | `~~incident management` | PagerDuty | — |
| CI/CD | `~~CI/CD` | — | — |
| Hosting / deploy | — | — | Vercel |
| Design | — | — | Figma |
| Browser automation | — | — | Playwright |
| Framework docs | — | — | Context7, Next.js DevTools |

Other options in each category: Microsoft Teams (chat), Bitbucket (source control), Shortcut or ClickUp (project tracker), Confluence or Guru (knowledge base), New Relic or Grafana (monitoring), Opsgenie or Incident.io (incident management), CircleCI or GitHub Actions (CI/CD).
