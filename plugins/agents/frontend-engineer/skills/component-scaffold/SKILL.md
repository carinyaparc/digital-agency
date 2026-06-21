---
name: component-scaffold
description: >
  Use when the user wants to create a new React/Next.js component that
  follows the target repo's existing conventions (naming, folder, styling
  approach) rather than a generic template. Do NOT use for full page/route
  creation or content-model changes (e.g. Payload collections).
license: MIT
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
argument-hint: "<ComponentName> [section|ui|form]"
---

# Component scaffold

Creates a new component that matches conventions already present in the
repo, not a generic boilerplate template.

## Steps

1. Find 2–3 existing components of the same kind (`section`, `ui`, or
   `form`) in the repo.
2. Match their conventions exactly: import style, props typing, whether
   `"use client"` is used, file naming, export style, and styling approach
   (Tailwind classes vs. CSS modules vs. UI primitives).
3. Create the new component in the same directory pattern as its peers.
4. If the repo uses TypeScript, type the props explicitly — no `any`.
5. Do not add the component to a barrel/index file unless existing
   sibling components already do so.
6. Report the file path created, which existing components it was modeled
   on, and anything you couldn't confidently infer — ask rather than guess.

## Output

State the file path, then show the full component code.
