# Ejemplo de Chatgpt
from multiprocessing import Process, Queue

# Función del proceso productor
def productor(q):
    q.put('Mensaje desde el productor')

# Función del proceso consumidor
def consumidor(q):
    mensaje = q.get()
    print(f'Consumidor recibió: {mensaje}')

if __name__ == '__main__':
    cola = Queue()  # Creamos la queue

    p1 = Process(target=productor, args=(cola,))
    p2 = Process(target=consumidor, args=(cola,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()