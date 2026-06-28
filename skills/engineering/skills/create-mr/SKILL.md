---
name: create-mr
description: >
  Creates a merge request or pull request for the current branch with generated
  title, description, labels, and reviewer suggestions. Use after implementation.
  Do NOT use for code review (code-review) or task implementation (implement).
license: MIT
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
  - Shell
argument-hint: "[story-id]"
---

# Create MR

Follow [prompts/run.prompt.md](prompts/run.prompt.md).
