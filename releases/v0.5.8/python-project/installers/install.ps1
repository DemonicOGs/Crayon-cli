$ErrorActionPreference = "Stop"
Write-Host "Installing Crayon CLI v0.5.8 (Python CLI)" -ForegroundColor Cyan
$python = Get-Command py -ErrorAction SilentlyContinue
if ($python) {
  py -3.10 -m pip install .
} else {
  $python = Get-Command python -ErrorAction SilentlyContinue
  if (-not $python) { throw "Python 3.10+ is required. Install it from https://www.python.org/downloads/" }
  python -m pip install .
}
crayon doctor
Write-Host "Installation complete." -ForegroundColor Green
