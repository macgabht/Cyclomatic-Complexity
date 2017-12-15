if %1% == 8 goto worker8


:worker8
	start cmd /c/documents/cc python worker.py
	start cmd /c/documents/cc python worker.py
	start cmd /c/documents/cc python worker.py
	start cmd /c/documents/cc python worker.py
	start cmd /c/documents/cc python worker.py
	start cmd /c/documents/cc python worker.py
	start cmd /c/documents/cc python worker.py
	start cmd /c/documents/cc python worker.py
	
	goto done

:done