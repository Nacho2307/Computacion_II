import os
import time

hijo_pid = os.fork()

if hijo_pid == 0:
    print(f"Hijo (PID: {os.getpid()}) terminando inmediatamente")
    exit(0)
elif hijo_pid > 0:
    # Código del padre
    print(f"Padre (PID: {os.getpid()}) creado hijo (PID: {hijo_pid})")
    print("El hijo ahora es zombi (verificar con 'ps aux | grep Z')")
    time.sleep(10)
    os.waitpid(hijo_pid, 0)
    print("Padre ha recogido el estado del hijo, ya no es zombi")
else:
    print("Error al crear hijo")
    exit(1)