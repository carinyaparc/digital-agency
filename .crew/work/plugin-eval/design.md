---
type: Design
mode: walking-skeleton
epic: plugin-eval
epic_id: AGENCY15
version: '0.2'
owner: Jonathan D'Addia
status: Draft
last_updated: 2026-06-28
related:
  - .crew/steering/solution.md
  - .crew/steering/backlog.md
  - .crew/work/plugin-eval/tasks.md
---

# Design -- Plugin Eval (AGENCY15)

Design for epic AGENCY15 at `.crew/work/plugin-eval/`. Architecture-wide patterns
are authoritative in [`.crew/steering/solution.md`](../../steering/solution.md).

**Intent.** Replace **eval-grader** with a single repo-local skill —
`.agents/skills/plugin-eval/SKILL.md` — that runs live eval sessions and grades
`evals/evals.json`, following the same shape as
[vercel-plugin-eval](https://github.com/vercel/vercel-plugin/blob/main/.claude/skills/vercel-plugin-eval/SKILL.md):
one markdown file, Bash commands in the conversation, no companion assets or scripts.

**Why not extra files?** The first draft over-engineered: fixture trees,
`catalog.json`, and report templates belong *inside* the skill (or are created
ad hoc by Bash at run time). Vercel proves that works. This repo already has
per-skill `evals/evals.json` and `trigger-queries.json` — those are the data;
plugin-eval is the procedure.

Completes the eval toolchain under AGENCY03 (repo-local tooling migration).

## 1. The slice

One maintainer invokes **plugin-eval** for a target skill path (e.g.
`skills/engineering/skills/design/`), launches a live Claude Code session,
executes prompts from that skill's `evals/evals.json`, grades each assertion
with quoted evidence from session outputs, and writes `.notes/COVERAGE.md`.
eval-grader is removed; contributor docs point at the new skill.

**Does not yet work:** CI batch runs, managed-agent evals, evals for skills
that do not yet ship an `evals/` folder.

## 2. Files shipped

| Path | Label | Purpose |
| ---- | ----- | ------- |
| `.agents/skills/plugin-eval/SKILL.md` | NEW | Hard rules, Quick Start bash, what to monitor, grading steps, coverage report outline, cleanup — all inline |
| `.agents/agents/eval-grader.md` | REMOVE | Superseded |
| `.agents/README.md` | EVOLVE | Tooling table |
| `.agents/skills/skills-qa/SKILL.md` | EVOLVE | eval-grader → plugin-eval |
| `CONTRIBUTING.md`, `AGENTS.md`, `README.md`, `CHANGELOG.md` | EVOLVE | Eval workflow refs |
| `skills/**/evals/evals.json` | KEEP | Existing per-skill eval definitions — no schema change |
| `skills/**/evals/trigger-queries.json` | KEEP | Existing trigger expectations |
| `agents/*/skills/validate/SKILL.md` | EVOLVE | Citation path (via `sync-agent-skills.py`) |

**Not shipped:** `assets/`, `scenarios/catalog.json`, fixture workspaces in
git, shell scripts, marketplace entries.

## 3. Acceptance gates

### 3.1 End-to-end path

- [ ] `.agents/skills/plugin-eval/SKILL.md` exists with DO NOT rules, Quick Start,
  monitor/grade instructions, and Coverage Report section (vercel shape).
- [ ] Live session run against one skill with `evals/` completes; `.notes/COVERAGE.md`
  has assertion matrix with ≥1 PASS and quoted evidence.

### 3.2 Workspace model

- [ ] SKILL.md documents one of: run **in this repo** (`.agents/` + `skills/` on
  disk), or timestamped clone under `~/dev/digital-agency-testing/` — no
  version-controlled fixture tree.

### 3.3 Deprecation

- [ ] `eval-grader.md` removed; grep finds no live refs to `eval-grader` or
  `agency-builder-hub/agents/eval-grader` outside CHANGELOG.

### 3.4 Quality gates

- [ ] skills-qa still documented as complementary (design review, not runtime eval).
- [ ] No new files under `.agents/skills/plugin-eval/` besides `SKILL.md`.

## 4. What this epic did NOT deliver

- CI / automated eval pipeline
- `catalog.json` or committed fixture workspaces
- `COVERAGE.template.md` — report structure lives in SKILL.md §Coverage Report
- New `evals/` for skills that lack them
- Managed-agent or headless eval path (AGENCY08+)
- Cursor-specific debug-log monitoring (best-effort transcript grading only)

## 5. SKILL.md contents (design contract)

Everything below is **sections inside the single file**, not separate artefacts.

| Section | Purpose |
| ------- | ------- |
| **DO NOT** | No `--print`, no skip-permissions, no `/tmp/`, no eval scripts, timestamp slugs |
| **Quick Start** | `mkdir` / clone repo, load `.agents/`, WezTerm spawn, find debug log |
| **What to monitor** | Debug log greps; files written under `.crew/work/` or `docs/work/` per skill |
| **Grading** | Read `evals/evals.json`; PASS/FAIL table with quoted evidence; eval-quality notes (from eval-grader) |
| **Trigger queries** | Optional: note `trigger-queries.json` checks where host signal exists |
| **Skills with evals** | Inline markdown table — design, tasks, backlog, validate paths |
| **Coverage Report** | `.notes/COVERAGE.md` outline: session index, assertion matrix, issues |
| **Cleanup** | `rm -rf ~/dev/digital-agency-testing/...` when using isolated workspaces |

**Architecture fit:** `.agents/` stays repo-local (`solution.md §1.2`, §10.2).
Grading reads skill sources under `skills/`, not bundled copies under `agents/`.

## 6. Handoff

**Stable on close:** plugin-eval SKILL.md as the sole eval entry point.

**Next:** `tasks write plugin-eval`; add AGENCY15 to backlog when tracking formally.

**Open question:** Run evals in-repo vs isolated clone — pick one in SKILL.md
Quick Start (recommend in-repo first; this catalogue *is* the workspace).
