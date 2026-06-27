# Brand Plugin

Brand practice for Carinya Parc Digital Services — visual identity and voice
guidelines agents can read from `docs/brand/`. Works in Cursor and Claude Code;
standalone with repo context, richer when MCP connectors are connected for
discovery.

## Installation

Install from this marketplace in Cursor Settings → Plugins, or add the plugin path in Claude Code.

## Skills overview

| Skill | Modes | Description | Artefact |
| ----- | ----- | ----------- | -------- |
| **brand-guide** | write, review, refine | Visual identity — colors, type, logo, UI tokens | `docs/brand/brand-guide.md` |
| **brand-voice** | discover, write, review, refine, enforce | Voice lifecycle and on-brand copy | `docs/brand/brand-voice.md`, `discovery-report.md`, inline content |

Invoke with mode first: `/brand-guide write`, `/brand-voice discover`, `/brand-voice enforce draft a LinkedIn post…`

## Where files live in your project

```text
docs/brand/
├── brand-guide.md          # Visual identity
├── brand-voice.md          # Voice, tone, terminology
├── discovery-report.md     # Optional — brand-voice discover
└── brand.local.md          # Gitignored settings (platforms, strictness)
```

Full path and boundary rules: [brand conventions](skills/references/brand-conventions.md).

## Typical flow

```text
brand-voice discover → brand-voice write → brand-voice review
                              ↓
                    (team resolves open questions)
                              ↓
                    brand-voice refine → brand-voice enforce (ongoing)

brand-guide write  (parallel — especially with Figma connected)
```

## Example workflows

### Discover brand materials

```
/brand-voice discover
```

Searches connected platforms; saves `docs/brand/discovery-report.md` when approved.

### Generate voice guidelines

```
/brand-voice write --from discovery-report
```

Produces `docs/brand/brand-voice.md` with We are / We are not, tone matrix, terminology.

### Write visual brand guide

```
/brand-guide write --from figma
```

Produces `docs/brand/brand-guide.md` with colors, typography, and UI tokens.

### Apply voice to content

```
/brand-voice enforce write a cold outreach email to a CTO about our platform
```

Loads `brand-voice.md` and generates on-brand copy.

## Standalone + supercharged

| What you can do | Standalone | Supercharged with |
| ----------------- | ---------- | ------------------- |
| brand-voice write | Paste docs or describe voice | Discovery report from **discover** |
| brand-voice discover | Manual file list | Notion, Confluence, Slack, Figma, Fireflies |
| brand-guide write | Paste hex/fonts | Figma variables and styles |
| brand-voice enforce | Paste guidelines once | Existing `brand-voice.md` in repo |

See [CONNECTORS.md](CONNECTORS.md) for bundled MCP servers.

## Related plugins

- **product-management** — strategy and comms skills; use **brand-voice enforce** for on-brand stakeholder updates
- **engineering** / **frontend-engineer** — **brand-guide** supplies UI tokens for implementation

## License

MIT — (c) Carinya Parc Pty Ltd.
