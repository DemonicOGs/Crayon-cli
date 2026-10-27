# Crayon CLI v0.5.8 — npm global launcher

The `crayon` command is exposed by npm; actual CLI functionality is implemented in Python.

## Global installation

After `crayon-cli@0.5.8` is published to npm:

```sh
npm install -g crayon-cli
crayon --version
crayon doctor
```

Requires Node.js 18+ and Python 3.10+. On Windows the launcher checks `py -3`, `python`, and `python3`. On Linux/macOS it checks `python3` and `python`. Set `CRAYON_PYTHON` to use a specific interpreter.

## Install from this checkout

From the project root:

```sh
python -m pip install .
npm install -g ./npm
crayon --version
```

Model weights are not bundled. Model-specific dependencies and the Python inference backend must be installed separately as described by the project documentation. Creating this archive does not publish the package to npm.
