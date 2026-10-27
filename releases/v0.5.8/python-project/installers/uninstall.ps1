$ErrorActionPreference = "Stop"
python -m pip uninstall -y crayon-cli
Write-Host "Crayon CLI package removed. User configuration under ~/.crayon was preserved."
