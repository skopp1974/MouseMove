Start-Process powershell -ArgumentList "-NoProfile -ExecutionPolicy Bypass -Command get-process -Name 'move' | Stop-Process -Force" -Verb RunAs