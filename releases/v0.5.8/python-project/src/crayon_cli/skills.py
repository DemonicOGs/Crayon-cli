from pathlib import Path
import os

def list_skills(cwd=None):
    roots = [
        Path(cwd or Path.cwd()) / ".crayon" / "skills",
        Path.home() / ".crayon" / "skills",
    ]
    result = []
    seen = set()
    for root in roots:
        if not root.exists():
            continue
        for skill_file in root.rglob("SKILL.md"):
            key = str(skill_file.resolve())
            if key in seen:
                continue
            seen.add(key)
            result.append({
                "name": skill_file.parent.name,
                "path": str(skill_file),
                "content": skill_file.read_text(encoding="utf-8"),
            })
    return result
