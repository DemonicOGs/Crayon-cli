import json
import os
from pathlib import Path

DEFAULTS = {
    "policy": "workspace-write",
    "output": "text",
    "skills": {"directories": []},
}

def config_paths():
    home = Path.home() / ".crayon" / "config.json"
    project = Path.cwd() / ".crayon" / "config.json"
    return {"user": str(home), "project": str(project)}

def _read(path):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON in {path}: {exc}") from exc

def load_config():
    paths = config_paths()
    result = dict(DEFAULTS)
    result.update(_read(paths["user"]))
    result.update(_read(paths["project"]))
    return result
