# Crayon CLI v0.5.8 â€” npm global launcher

The `crayon` command is exposed by npm; actual CLI functionality is implemented in Python.

## Global installation

After `@lazarusrolando/crayoncli@0.5.8` is published to npm:

```sh
npm install -g @lazarusrolando/crayoncli
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


## Interactive startup

Running `crayon` without arguments opens the interactive terminal interface. In this scaffold build, prompts are captured as request envelopes; a model inference backend is not bundled or connected, so it will not generate AI answers until that backend is integrated. Use `/help` for built-in commands and `/exit` to quit.

