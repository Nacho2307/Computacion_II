# ejercicio_kill_hijo_a_padre.py
import os
import signal
import time

def handler(signum, frame):
    print(f"Padre recibió señal {signum} del hijo")

signal.signal(signal.SIGUSR1, handler)

pid = os.fork()

if pid == 0:
    # Proceso hijo
    time.sleep(1)
    os.kill(os.getppid(), signal.SIGUSR1)
    print("Hijo envió SIGUSR1 al padre")
else:
    # Proceso padre
    print(f"Padre esperando señal de PID {pid}")
    signal.pause()
    print("Padre termina")