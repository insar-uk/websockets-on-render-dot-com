# Sockets on render.com
Very basic setup to make sure I can use websockets on render.com

## Setup venv and dependencies
``` PowerShell
python -m venv websockets-venv 
.\websockets-venv\Scripts\Activate.ps1
pip install websockets 
# for testing:
pip install pytest

```

## Testing
is annoying with pytest and threading, so for this simple project just try it out

## Run the server
``` PowerShell
python -m app
```

## Run the client
``` PowerShell
# Open the html file with default browser
.\client.html
```

