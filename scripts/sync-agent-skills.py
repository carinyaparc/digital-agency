#!/usr/bin/env python3
"""
Re-sync each agent plugin's bundled skills from the skills source.

Agent plugins under plugins/agents/<slug>/skills/<name>/ are vendored
copies of plugins/skills/<discipline>/skills/<name>/. The plugins/skills/ tree
is the source of truth; run this after editing a skill there to propagate the
change into every agent that bundles it.

Usage: python3 scripts/sync-agent-skills.py
"""
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AGENTS = ROOT / "plugins" / "agents"
PRACTICES = ROOT / "plugins" / "skills"

# index every skill name -> source dir in practices (skip shared refs)
src_by_name: dict[str, Path] = {}
for sk in PRACTICES.glob("*/skills/*"):
    if sk.is_dir() and sk.name != "references":
        src_by_name[sk.name] = sk

synced = 0
missing: list[str] = []
for agent_dir in sorted(AGENTS.glob("*")):
    skills_dir = agent_dir / "skills"
    if not skills_dir.is_dir():
        continue

    disciplines_used: set[Path] = set()
    for bundled in sorted(skills_dir.iterdir()):
        if not bundled.is_dir() or bundled.name == "references":
            continue
        src = src_by_name.get(bundled.name)
        if not src:
            missing.append(str(bundled.relative_to(ROOT)))
            continue
        shutil.rmtree(bundled)
        shutil.copytree(src, bundled)
        synced += 1
        disciplines_used.add(src.parent.parent)

    for practice in disciplines_used:
        refs = practice / "skills" / "references"
        if refs.is_dir():
            dest = skills_dir / "references"
            if dest.exists():
                shutil.rmtree(dest)
            shutil.copytree(refs, dest)
            break

print(f"synced {synced} bundled skill dir(s) from plugins/skills/")
if missing:
    print("WARN: no skills source found for:", file=sys.stderr)
    for m in missing:
        print(f"  - {m}", file=sys.stderr)
    sys.exit(1)
