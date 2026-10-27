import subprocess
from pathlib import Path

def _git(args):
    proc = subprocess.run(["git", *args], text=True, capture_output=True)
    if proc.returncode:
        raise RuntimeError(proc.stderr.strip() or f"git exited with {proc.returncode}")
    return proc.stdout.strip()

def worktree_command(args):
    if not args:
        raise ValueError("Usage: crayon worktree create <path> [branch] | list | remove <path>")
    sub = args[0]
    if sub == "list":
        raw = _git(["worktree", "list", "--porcelain"])
        records = []
        for block in filter(None, raw.split("\\n\\n")):
            record = {}
            for line in block.splitlines():
                key, _, value = line.partition(" ")
                record[key] = value or True
            records.append(record)
        return records
    if sub == "create":
        if len(args) < 2:
            raise ValueError("Usage: crayon worktree create <path> [branch]")
        target = Path(args[1]).expanduser().resolve()
        branch = args[2] if len(args) > 2 else "crayon/" + target.name.replace(" ", "-")
        if target.exists():
            raise ValueError(f"Target path already exists: {target}")
        _git(["worktree", "add", "-b", branch, str(target)])
        return {"created": str(target), "branch": branch}
    if sub == "remove":
        if len(args) < 2:
            raise ValueError("Usage: crayon worktree remove <path>")
        target = Path(args[1]).expanduser().resolve()
        _git(["worktree", "remove", str(target)])
        return {"removed": str(target)}
    raise ValueError("Usage: crayon worktree create <path> [branch] | list | remove <path>")
