import threading
import signal
import os
import time

# Evento global que será usado por todos los hilos
stop_event = threading.Event()

def handler(signum, frame):
    print(f"Señal {signum} recibida. Solicitando parada...")
    stop_event.set()

# Worker thread
def worker():
    while not stop_event.is_set():
        print(f"[{threading.current_thread().name}] trabajando...")
        time.sleep(1)
    print(f"[{threading.current_thread().name}] registrado log antes de detenerse.")
    print(f"[{threading.current_thread().name}] detenido.")

# Registrar señales SIGINT y SIGTERM en el hilo principal
signal.signal(signal.SIGINT, handler)
signal.signal(signal.SIGTERM, handler)

# Crear e iniciar varios hilos
threads = [threading.Thread(target=worker, name=f"Hilo-{i}") for i in range(3)]
for t in threads:
    t.start()

# Esperar que todos terminen
for t in threads:
    t.join()
print("Todos los hilos terminaron.")