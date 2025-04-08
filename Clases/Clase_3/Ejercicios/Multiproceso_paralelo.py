import os
import time

def hijo(num):
    print(f"Hijo {num} (PID: {os.getpid()}) ejecutando tarea...")
    time.sleep(num)
    print(f"Hijo {num} terminado")
    exit(0)

hijos = []
for i in range(3):
    pid = os.fork()
    if pid == 0:
        hijo(i+1)
    elif pid > 0:
        hijos.append(pid)
    else:
        print("Error al crear hijo")
        exit(1)

for pid in hijos:
    os.waitpid(pid, 0)

print("Todos los hijos han terminado")