import os
import time

def hijo(num):
    print(f"Soy el hijo {num}, mi PID es {os.getpid()}")
    time.sleep(2)
    exit(0)

hijo1 = os.fork()

if hijo1 == 0:
    hijo(1)
elif hijo1 < 0:
    print("Error al crear primer hijo")
    exit(1)

hijo2 = os.fork()

if hijo2 == 0:
    hijo(2)
elif hijo2 < 0:
    print("Error al crear segundo hijo")
    exit(1)

os.waitpid(hijo1, 0)
os.waitpid(hijo2, 0)

print("Ambos hijos han terminado")