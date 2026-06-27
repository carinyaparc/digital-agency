<!--
TEMPLATE — do not write user data here.

This file ships with the plugin and shows the structure the config should have.
It is replaced on every plugin update. Never write user data here.

Future cold-start and community-install flows will copy a populated profile to:
  ~/.claude/plugins/config/carinya-digital/agency-builder-hub/CLAUDE.md
-->

# Agency Builder Hub Profile

*Populated by future cold-start when community skill install ships.*

---

## Built-in plugins

These plugins ship with the digital-agency reference and are managed by `/plugin`,
not by this hub. Future `uninstall` and `disable` skills will refuse to touch
skills that resolve into these directories.

- `engineering`
- `product-management`
- `brand`
- `frontend-engineer`
- `senior-frontend-engineer`
- `product-manager`
- `agency-builder-hub`
- Connector plugins under `plugins/connectors/`

---

## Shared guardrails

**Draft for review by default.** Agency skills produce work for qualified humans
to verify before merge, publish, or client delivery unless the skill explicitly
declares a lower-stakes `output_class` and the target repo agrees.

**Target repo wins.** When the repository an agent works in defines conventions
(`AGENTS.md`, `CLAUDE.md`, lint rules), those override plugin defaults.

**Trust surface is declared.** Elevated tools (Bash, deploy MCPs, broad Write)
require explicit justification in the skill and in QA.

---

## Hub tooling (v0)

| Tool | Purpose |
| --- | --- |
| **eval-grader** | Grade eval batch output against `evals/evals.json` |
| **skills-qa** | Evaluate a skill against the Agency Skill Design Framework |

Community registry browse, install, and auto-update — not yet shipped.
