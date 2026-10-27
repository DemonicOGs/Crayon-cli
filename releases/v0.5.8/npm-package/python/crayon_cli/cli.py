import argparse
import json
import sys
import os
from . import __version__
from .config import config_paths, load_config
from .doctor import run_doctor
from .instructions import load_project_instructions
from .policy import active_policy, evaluate_command
from .skills import list_skills
from .worktrees import worktree_command


def _emit(value, as_json=False):
    if as_json:
        print(json.dumps(value, indent=2, ensure_ascii=False))
    elif isinstance(value, str):
        print(value)
    else:
        print(json.dumps(value, indent=2, ensure_ascii=False))


def build_parser():
    parser = argparse.ArgumentParser(prog="crayon", description=f"Crayon CLI v{__version__} (Python)")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON")
    parser.add_argument("--prompt", help="Prepare a non-interactive request envelope")
    sub = parser.add_subparsers(dest="command")
    doctor_parser = sub.add_parser("doctor", help="Check the local environment")
    doctor_parser.add_argument("--json", action="store_true", default=argparse.SUPPRESS, help=argparse.SUPPRESS)
    cfg = sub.add_parser("config", help="Inspect configuration")
    cfg.add_argument("--json", action="store_true", default=argparse.SUPPRESS, help=argparse.SUPPRESS)
    cfg.add_argument("action", choices=("show", "paths"), nargs="?", default="show")
    instructions_parser = sub.add_parser("instructions", help="Load project instruction files")
    instructions_parser.add_argument("--json", action="store_true", default=argparse.SUPPRESS, help=argparse.SUPPRESS)
    skills = sub.add_parser("skills", help="Discover reusable skills")
    skills.add_argument("--json", action="store_true", default=argparse.SUPPRESS, help=argparse.SUPPRESS)
    skills.add_argument("action", choices=("list",), nargs="?", default="list")
    policy = sub.add_parser("policy", help="Inspect/check execution policy")
    policy.add_argument("--json", action="store_true", default=argparse.SUPPRESS, help=argparse.SUPPRESS)
    policy.add_argument("action", choices=("show", "check"), nargs="?", default="show")
    policy.add_argument("command_text", nargs=argparse.REMAINDER)
    wt = sub.add_parser("worktree", help="Manage isolated Git worktrees")
    wt.add_argument("--json", action="store_true", default=argparse.SUPPRESS, help=argparse.SUPPRESS)
    wt.add_argument("args", nargs=argparse.REMAINDER)
    return parser


def _interactive():
    print(f"Crayon CLI v{__version__}")
    print("Local coding assistant interface. Type /help for commands, /exit to quit.")
    print("AI inference backend is not configured in this package build; prompts cannot be answered by a model yet.")
    while True:
        try:
            line = input("\ncrayon> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            return 0
        if not line:
            continue
        command = line.lower()
        if command in ("/exit", "/quit", "exit", "quit"):
            print("Goodbye!")
            return 0
        if command in ("/help", "help", "?"):
            print("Commands: /help, /doctor, /config, /instructions, /skills, /policy, /exit")
            print("Enter a coding prompt to prepare a request; a model backend is required for an AI response.")
        elif command == "/doctor":
            _emit(run_doctor())
        elif command == "/config":
            _emit(load_config())
        elif command == "/instructions":
            _emit(load_project_instructions())
        elif command == "/skills":
            _emit(list_skills())
        elif command == "/policy":
            _emit(active_policy())
        else:
            request = {
                "kind": "crayon.request.v1",
                "version": __version__,
                "prompt": line,
                "cwd": os.getcwd(),
                "policy": load_config().get("policy", "workspace-write"),
                "instructions": load_project_instructions(),
            }
            print("\nPrompt captured, but no inference backend is configured. Request envelope:")
            print(json.dumps(request, indent=2, ensure_ascii=False))


def main():
    parser = build_parser()
    if len(sys.argv) == 1 and sys.stdin.isatty():
        return _interactive()
    args = parser.parse_args()
    try:
        if args.prompt is not None:
            request = {
                "kind": "crayon.request.v1",
                "version": __version__,
                "prompt": args.prompt,
                "cwd": os.getcwd(),
                "policy": load_config().get("policy", "workspace-write"),
                "instructions": load_project_instructions(),
            }
            _emit(request if args.json else "Prepared request envelope (model adapter not wired):\n" + json.dumps(request, indent=2), args.json)
            return 0
        if args.command == "doctor":
            result = run_doctor()
        elif args.command == "config":
            result = config_paths() if args.action == "paths" else load_config()
        elif args.command == "instructions":
            result = load_project_instructions()
        elif args.command == "skills":
            result = list_skills()
        elif args.command == "policy":
            result = active_policy() if args.action == "show" else evaluate_command(" ".join(args.command_text))
        elif args.command == "worktree":
            result = worktree_command(args.args)
        else:
            parser.print_help()
            return 0
        _emit(result, args.json)
        return 0
    except Exception as exc:
        payload = {"error": str(exc)}
        print(json.dumps(payload) if args.json else f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
