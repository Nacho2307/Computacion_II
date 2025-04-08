import os
import time

NUM_CLIENTES = 5

def atender_cliente(num):
    print(f"Servidor atendiendo cliente {num} (PID: {os.getpid()})")
    time.sleep(3)
    print(f"Cliente {num} atendido")
    exit(0)

for i in range(NUM_CLIENTES):
    pid = os.fork()
    if pid == 0:
        atender_cliente(i+1)
    elif pid < 0:
        print("Error al crear proceso hijo")
        exit(1)

for _ in range(NUM_CLIENTES):
    os.wait()

print("Todos los clientes han sido atendidos")