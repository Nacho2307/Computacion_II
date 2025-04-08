import os
import time

def hijo(num):
    print(f"Hijo {num} (PID: {os.getpid()}) ejecutando tarea...")
    time.sleep(2)
    print(f"Hijo {num} terminado")
    exit(0)

hijo1 = os.fork()

if hijo1 == 0:
    hijo(1)
elif hijo1 < 0:
    print("Error al crear primer hijo")
    exit(1)

os.waitpid(hijo1, 0)

hijo2 = os.fork()

if hijo2 == 0:
    hijo(2)
elif hijo2 < 0:
    print("Error al crear segundo hijo")
    exit(1)

os.waitpid(hijo2, 0)

print("Ambos hijos han terminado en secuencia")