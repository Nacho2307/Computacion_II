import threading
import signal
import os
import time

# Evento que es usado por todos los hilos
stop_event = threading.Event()

def handler(signum, frame):
    print(f"Señal {signum} recibida. Solicitando parada...")
    stop_event.set()

# Registra las señales SIGINT y SIGTERM en el hilo principal
signal.signal(signal.SIGINT, handler)  # Ctrl+C
signal.signal(signal.SIGTERM, handler) # SIGTERM

# Worker thread
def worker():
    while not stop_event.is_set():
        print(f"[{threading.current_thread().name}] trabajando...")
        time.sleep(1)
    print(f"[{threading.current_thread().name}] detenido.")

# Crea e inicia varios hilos
threads = [threading.Thread(target=worker, name=f"Hilo-{i}") for i in range(3)]
for t in threads:
    t.start()

# Espera que terminen
for t in threads:
    t.join()
print("Todos los hilos terminaron.")