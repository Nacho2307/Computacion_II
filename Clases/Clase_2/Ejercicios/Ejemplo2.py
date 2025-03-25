# Hijo ejecuta ls -la

import os

pid = os.fork()

if pid == 0:
    os.execlp("ls", "ls", "-l" )
else:
    os.wait() # El padre espera a que el hijo termine
    print(f"El proceso hijo termino")
