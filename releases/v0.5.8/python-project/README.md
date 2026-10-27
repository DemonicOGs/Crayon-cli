# Crayon CLI v0.5.8 — Python CLI

This fresh v0.5.8 scaffold implements the **CLI layer in Python**, rather than Node.js. It does not inspect, modify, or depend on the existing v0.5.7 ZIP.

## Included

- Python command-line entry point: `crayon`
- Execution policy profiles: `read-only`, `workspace-write`, `unrestricted` (explicit opt-in)
- Parent-directory discovery for `AGENTS.md` and `CRAYON.md`
- Non-interactive `--prompt` mode and JSON output
- User/project configuration
- Reusable `SKILL.md` discovery
- Git worktree create/list/remove commands
- `crayon doctor` environment diagnostics
- Windows PowerShell and POSIX shell installer scripts

## Requirements

- Python 3.10+
- Git for worktree commands
- The actual Crayon inference service/model runtime must be supplied separately; this scaffold does not bundle models or implement a model adapter.

## Install from this folder

Windows PowerShell:
```powershell
.\installers\install.ps1
```

Linux/macOS:
```sh
sh installers/install.sh
```

Or install directly:
```sh
python -m pip install .
crayon doctor
```

## Quick test

```sh
crayon --help
crayon doctor
crayon config show
crayon instructions
crayon skills list
crayon policy show
crayon --prompt "Summarize the project" --json
```

## Configuration

- User config: `~/.crayon/config.json`
- Project config: `.crayon/config.json` (overrides user settings)

Example:
```json
{
  "policy": "workspace-write",
  "output": "text",
  "skills": {"directories": []}
}
```

## Safety and integration notes

Policy checks are advisory; they are not an operating-system sandbox. Use OS/container isolation for untrusted code. Prompt mode currently emits a structured request envelope and does not invoke a model. A production release must connect this envelope to the actual Crayon inference client and test the complete CLI/backend lifecycle.


## Package installation

Crayon is configured as a Python package with the `crayon` console command. After publishing `crayon-cli` v0.5.8 to PyPI, install it globally for all users with a current pipx version and an elevated terminal:

```sh
pipx install --global crayon-cli==0.5.8
crayon --version
crayon doctor
```

For a per-user install, use `pipx install crayon-cli==0.5.8`. For a local checkout, run `python -m pip install .`. See [Package installation](docs/PACKAGE_INSTALLATION.md) for upgrade, uninstall, and publishing instructions. The package has not been published to PyPI by generating this source archive.


## v0.5.8 npm global package

The separate `npm/` folder contains a minimal JavaScript launcher and a bundled copy of the Python CLI. After publishing `crayon-cli@0.5.8` to npm, install globally:

```sh
npm install -g crayon-cli
crayon --version
crayon doctor
```

Requires Node.js 18+ and Python 3.10+. The package is not published by creating this ZIP. Full feature parity with the original v0.5.7 source has not been verified because that source archive was not available as the baseline.
