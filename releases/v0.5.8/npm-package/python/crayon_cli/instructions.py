from pathlib import Path

def load_project_instructions(start_dir=None):
    directory = Path(start_dir or Path.cwd()).resolve()
    found = []
    while True:
        for name in ("AGENTS.md", "CRAYON.md"):
            candidate = directory / name
            if candidate.is_file():
                found.append({"path": str(candidate), "content": candidate.read_text(encoding="utf-8")})
        if directory.parent == directory:
            break
        directory = directory.parent
    found.reverse()
    return found
