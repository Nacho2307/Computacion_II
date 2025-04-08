import os
import time
import subprocess

hijo_pid = os.fork()

if hijo_pid == 0:
    # Código del hijo que se volverá huérfano
    print(f"Proceso hijo (PID: {os.getpid()}) iniciado")

    time.sleep(2)

    print(f"Hijo ahora es huérfano (PPID: {os.getppid()})")

    print("Ejecutando comando no supervisado...")
    with open('comandos.log', 'w') as f:
        subprocess.run(["echo", "Este comando se ejecuta sin control del padre"], stdout=f)
        subprocess.run(["date"], stdout=f)
    
    print("Comando ejecutado, ver contenido de comandos.log")
elif hijo_pid > 0:
    print(f"Proceso padre (PID: {os.getpid()}) terminando...")
    exit(0)
else:
    print("Error al crear proceso hijo")
    exit(1)