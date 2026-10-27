import re
from .config import load_config

PROFILES = {
    "read-only": "Rejects commands likely to modify files or system state.",
    "workspace-write": "Allows ordinary workspace edits and flags risky commands for review.",
    "unrestricted": "No restrictions in this policy layer; use only in a trusted isolated environment.",
}
DANGEROUS = [
    re.compile(r"\brm\s+-rf\b", re.I),
    re.compile(r"\bsudo\b", re.I),
    re.compile(r"\bmkfs\b", re.I),
    re.compile(r"\bdd\s+if=", re.I),
    re.compile(r"\bshutdown\b", re.I),
    re.compile(r"\breboot\b", re.I),
    re.compile(r"\bformat\s+[a-z]:", re.I),
    re.compile(r"\bRemove-Item\b.*-Recurse.*-Force", re.I),
    re.compile(r">\s*/dev/sd", re.I),
]
WRITES = [
    re.compile(r"\b(rm|mv|cp|mkdir|touch|chmod|chown|tee)\b", re.I),
    re.compile(r"\b(npm\s+(install|uninstall)|pip\s+install|git\s+(checkout|reset|clean|merge|rebase))\b", re.I),
    re.compile(r">{1,2}"),
]

def active_policy():
    name = load_config().get("policy", "workspace-write")
    return {"name": name, "description": PROFILES.get(name, PROFILES["workspace-write"]),
            "available_profiles": list(PROFILES)}

def evaluate_command(command, profile=None):
    profile = profile or load_config().get("policy", "workspace-write")
    if profile not in PROFILES:
        return {"allowed": False, "decision": "deny", "reason": f"Unknown policy profile: {profile}"}
    if profile == "unrestricted":
        return {"allowed": True, "decision": "allow", "reason": "Unrestricted profile explicitly selected."}
    if any(rx.search(command) for rx in DANGEROUS):
        return {"allowed": False, "decision": "review", "reason": "Potentially destructive or system-wide command."}
    if profile == "read-only" and any(rx.search(command) for rx in WRITES):
        return {"allowed": False, "decision": "deny", "reason": "Write-like command blocked by read-only profile."}
    if any(rx.search(command) for rx in WRITES):
        return {"allowed": False, "decision": "review", "reason": "Write-like command should be reviewed."}
    return {"allowed": True, "decision": "allow", "reason": "No policy rule matched."}
