---
name: code-review
description: >
  Use when the user wants a code review of a branch, PR, or diff against
  design.md and tasks.md acceptance criteria, or to address review feedback
  without changing behaviour (code-review fix). Do NOT use to implement
  (implement) or epic completion sign-off (validate).
license: MIT
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
  - Shell
argument-hint: "[fix] [branch-or-pr-or-review-output]"
---

# Code review

Review a branch, PR, or diff; or address findings from a prior review.

## Sub-agents

For large diffs or pre-PR review, spawn in parallel (Claude Code agents or Cursor Task):

| Agent | File | Focus |
| ----- | ---- | ----- |
| tasks-ac-reviewer | [agents/tasks-ac-reviewer.md](agents/tasks-ac-reviewer.md) | Gherkin in `docs/work/{epic}/tasks.md` vs diff |
| design-drift-reviewer | [agents/design-drift-reviewer.md](agents/design-drift-reviewer.md) | Scope vs `docs/work/{epic}/design.md` |

Merge agent outputs into one verdict. Default review scope: `git diff` unless the user specifies files.

## Conventions

[../backlog/references/delivery-conventions.md](../backlog/references/delivery-conventions.md)

## Router

1. Mode: default **review**, or `fix`.
2. One prompt under [prompts/](prompts/).

**review** (default) — [prompts/run.prompt.md](prompts/run.prompt.md).

**fix** — [prompts/fix.prompt.md](prompts/fix.prompt.md).

Pass branch, PR, diff, or review output after the mode token.
