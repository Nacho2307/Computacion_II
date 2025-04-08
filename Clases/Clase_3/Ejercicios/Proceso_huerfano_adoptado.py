import os
import time

hijo_pid = os.fork()

if hijo_pid == 0:
    print(f"Hijo (PID: {os.getpid()}) iniciado, PPID: {os.getppid()}")
    print("Hijo esperando 5 segundos...")
    time.sleep(5)
    print(f"Hijo ahora debería ser adoptado por init, PPID: {os.getppid()}")
elif hijo_pid > 0:
    print(f"Padre (PID: {os.getpid()}) creado hijo (PID: {hijo_pid})")
    print("Padre terminando inmediatamente...")
    exit(0)
else:
    print("Error al crear hijo")
    exit(1)