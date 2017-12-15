if %1% == 8 got to 8workers

:8workers
	start cmd /c python worker.py
	start cmd /c python worker.py
	start cmd /c python worker.py
	start cmd /c python worker.py
	start cmd /c python worker.py
	start cmd /c python worker.py
	start cmd /c python worker.py
	start cmd /c python worker.py
	start cmd /c python worker.py
	goto done

:done