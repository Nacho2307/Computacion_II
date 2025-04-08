import os

hijo_pid = os.fork()

if hijo_pid == 0:
    print("El hijo va a ejecutar 'ls -l'")
    os.execlp('ls', 'ls', '-l')
    print("Error al ejecutar exec")
    exit(1)
elif hijo_pid > 0:
    os.waitpid(hijo_pid, 0)
    print("El hijo ha terminado")
else:
    print("Error al crear hijo")
    exit(1)