![Crayon — Local AI Coding CLI](./crayon-cli.png)

# Crayon CLI v0.5.9

Crayon CLI v0.5.9 is a Python-based CLI scaffold distributed through npm. npm provides the global `crayon` launcher; the command-line behavior lives in the bundled Python package.

> **Scope note:** This archive is a scaffold, not a complete local-AI runtime. It does not bundle model weights or connect to an inference backend, so it cannot generate AI responses yet. Full feature parity with the earlier v0.5.7 implementation is not verified.

## Features included

- Global `crayon` launcher through npm, with Python interpreter discovery.
- `CRAYON_PYTHON` override for selecting a Python executable.
- Environment diagnostics with `crayon doctor`.
- Configuration inspection with `crayon config show` and `crayon config paths`.
- Project instruction discovery for `AGENTS.md` and `CRAYON.md`.
- Reusable skill discovery from `.crayon/skills` directories.
- Advisory command-policy profiles: `read-only`, `workspace-write`, and `unrestricted`.
- Git worktree operations: list, create, and remove.
- JSON output option and non-interactive prompt-envelope mode.

## Requirements

- Node.js 18 or newer for npm installation and launcher.
- Python 3.10 or newer.
- Git for worktree commands and the Git diagnostic.

## Install globally

After the package has been published to npm:

```sh
npm install -g @lazarusrolando/crayoncli
crayon --version
crayon doctor
```

The package name in this archive is **`@lazarusrolando/crayoncli`**. It is not named `crayon-cli`.

## Install from a local checkout

From the extracted project directory:

```sh
python -m pip install .
npm install -g ./npm
crayon --version
```

## Commands

```sh
crayon --version
crayon doctor
crayon config show
crayon config paths
crayon instructions
crayon skills
crayon policy
crayon worktree list
crayon worktree create ../my-worktree
crayon worktree remove ../my-worktree
```

For command details, run:

```sh
crayon --help
crayon <command> --help
```

Global options include `--json` for machine-readable output and `--prompt "..."` to prepare a non-interactive request envelope.

## Configuration

Crayon checks user configuration at `~/.crayon/config.json` and project configuration at `.crayon/config.json`. Project values override user values. The default policy is `workspace-write`.

The policy checks are advisory only; they are **not** an operating-system security sandbox.

## Current limitations and validation

- No model weights are included.
- The FastAPI inference backend and model runtime are not included or connected.
- The interactive terminal interface captures request envelopes; it does not produce AI answers without an integrated backend.
- Full v0.5.7 feature parity is not verified because the original complete v0.5.7 source was not available as the baseline for this packaging step.
- The package metadata says `0.5.9`, but the bundled Python `__version__` currently says `0.5.8`. Consequently, `crayon --version` may report `0.5.8`; update `python/crayon_cli/__init__.py` before publishing if `0.5.9` is intended to be the displayed version.
- Creating this archive does not publish it to npm.

## License

Apache-2.0. See `LICENSE`.
