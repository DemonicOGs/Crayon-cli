# Crayon CLI v0.5.8 — Package installation

Crayon is packaged as a Python distribution named `crayon-cli` and exposes the `crayon` command.

## Install from a published Python package index

Once `crayon-cli` v0.5.8 has been published to the Python Package Index (PyPI):

### Global installation for all users (pipx)

Use a current version of pipx that supports global installations. Run the command from an elevated terminal (Administrator on Windows, or with the required system permissions on Linux/macOS):

```sh
pipx install --global crayon-cli==0.5.8
crayon --version
crayon doctor
```

Upgrade and uninstall the global installation:

```sh
pipx upgrade --global crayon-cli
pipx uninstall --global crayon-cli
```

Global pipx installs expose the command in pipx's shared binary location; ensure that location is on the system `PATH`.

### Per-user isolated installation (pipx)

If you do not want to install for every user:

```sh
pipx install crayon-cli==0.5.8
crayon --version
crayon doctor
```

Upgrade and uninstall:

```sh
pipx upgrade crayon-cli
pipx uninstall crayon-cli
```

### Direct global pip installation (not recommended)

You can install into the active Python environment with elevated privileges:

```sh
python -m pip install crayon-cli==0.5.8
```

This may conflict with OS-managed Python packages. Prefer global pipx or a per-user pipx installation instead.

### Standard pip installation

```sh
python -m pip install crayon-cli==0.5.8
crayon --version
```

Upgrade and uninstall:

```sh
python -m pip install --upgrade crayon-cli
python -m pip uninstall crayon-cli
```

On systems that protect the system Python, use a virtual environment or `pipx` rather than forcing a system-wide install.

## Install from a local source checkout

From the directory containing `pyproject.toml`:

```sh
python -m pip install .
```

For editable development:

```sh
python -m pip install -e .
```

## Publishing the package

A maintainer should build and test the distribution, then upload it to PyPI using a trusted publishing workflow or an appropriately scoped API token. Do not upload secrets to source control.

```sh
python -m pip install --upgrade build
python -m build
```

Upload the generated `dist/` artifacts using the project's approved PyPI publishing workflow.

**Publication status:** this source scaffold does not establish that `crayon-cli` is already published on PyPI. The public `pipx install crayon-cli` command will work only after the package is published under that exact distribution name.

## Backend note

This package provides the Python CLI scaffold. The Crayon FastAPI inference service and model runtime must be packaged or installed separately before AI inference commands can work end-to-end.
