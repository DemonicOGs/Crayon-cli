# Crayon CLI v0.5.8 â€” Python CLI + npm launcher

## Highlights

- Python owns CLI behavior; JavaScript is limited to npm packaging and starting the Python entry point.
- npm package metadata exposes the global `crayon` command.
- Cross-platform Python discovery for Windows, Linux, and macOS, with `CRAYON_PYTHON` override.
- Codex-inspired execution policy profiles.
- `AGENTS.md` and `CRAYON.md` project instruction discovery.
- Non-interactive prompt mode and JSON output where implemented in the scaffold.
- Central configuration and reusable skill discovery.
- Git worktree management.
- `crayon doctor` diagnostics.
- Updated installation and release documentation.

## v0.5.7 feature-parity target

Features to retain include interactive chat and streaming, Python FastAPI inference, model discovery/download/switching, GGUF and Transformers runtimes, remote and browser backends, sessions/history, agent instructions and permission modes, file operations/search/indexing, memory, checkpoints/undo/restore, tests/builds, diagnostics, and multimodal image/audio/video/multi-file understanding where supported by the selected runtime.

## Validation and limitations

- The release ZIP includes the npm package, launcher, and bundled Python CLI scaffold.
- Python files are syntax-checked and the launcher is checked with Node.js when available.
- Windows/macOS end-to-end installation is not run in this environment.
- The original complete v0.5.7 source archive was not available as the baseline for this packaging step. Full v0.5.7 feature parity is therefore **not verified**, and the bundled Python CLI scaffold should not be represented as a full conversion of the original CLI.
- Model weights are not bundled. Backend/model execution requires the appropriate runtime dependencies and end-to-end testing.

## Install after npm publication

```sh
npm install -g @lazarusrolando/crayoncli
crayon --version
crayon doctor
```

Requires Node.js 18+ and Python 3.10+.

