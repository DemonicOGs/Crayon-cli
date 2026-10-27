import shutil
import subprocess
import sys
from . import __version__
from .config import config_paths, load_config

def _version(command, args):
    executable = shutil.which(command)
    if not executable:
        return None
    result = subprocess.run([executable, *args], text=True, capture_output=True)
    if result.returncode:
        return None
    return (result.stdout or result.stderr).strip().splitlines()[0]

def run_doctor():
    cfg = load_config()
    checks = [
        {"name": "Crayon CLI", "version": __version__, "ok": True},
        {"name": "Python", "version": sys.version.split()[0], "ok": sys.version_info >= (3, 10)},
        {"name": "Git", "version": _version("git", ["--version"]), "ok": bool(_version("git", ["--version"]))},
    ]
    return {
        "ok": all(item["ok"] for item in checks),
        "checks": checks,
        "config_paths": config_paths(),
        "active_policy": cfg.get("policy", "workspace-write"),
        "notes": [
            "The FastAPI inference backend/model runtime is not installed by this scaffold.",
            "Policy checks are advisory and are not an OS-level sandbox.",
        ],
    }
