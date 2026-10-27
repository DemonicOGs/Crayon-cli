#!/usr/bin/env node
"use strict";

// Node/npm provides installation and command shimming; CLI behavior lives in Python.
const { spawnSync } = require("node:child_process");
const fs = require("node:fs");
const path = require("node:path");

const root = path.resolve(__dirname, "..");
const pythonPackageRoot = path.join(root, "python");
const packageEntry = path.join(pythonPackageRoot, "crayon_cli", "__main__.py");

if (!fs.existsSync(packageEntry)) {
  console.error("Crayon installation is incomplete: Python package entry point is missing.");
  process.exit(1);
}

const candidates = process.env.CRAYON_PYTHON
  ? [process.env.CRAYON_PYTHON]
  : (process.platform === "win32" ? ["py", "python", "python3"] : ["python3", "python"]);

// Make the bundled package importable, then launch it as a module. Running cli.py
// directly breaks its relative imports (for example, `from . import __version__`).
const env = { ...process.env };
const existingPythonPath = env.PYTHONPATH;
env.PYTHONPATH = existingPythonPath
  ? `${pythonPackageRoot}${path.delimiter}${existingPythonPath}`
  : pythonPackageRoot;

for (const exe of candidates) {
  const args = exe === "py"
    ? ["-3", "-m", "crayon_cli", ...process.argv.slice(2)]
    : ["-m", "crayon_cli", ...process.argv.slice(2)];

  const result = spawnSync(exe, args, {
    stdio: "inherit",
    cwd: process.cwd(),
    env,
  });

  if (result.error && result.error.code === "ENOENT") continue;
  if (result.error) {
    console.error(`Could not start Python: ${result.error.message}`);
    process.exit(1);
  }
  process.exit(result.status === null ? 1 : result.status);
}

console.error("Crayon requires Python 3.10 or newer. Install Python and add it to PATH,");
console.error("or set CRAYON_PYTHON to the Python executable path.");
process.exit(127);
