# Crear proceso hijo con fork()

import os 

def creo_proceso():
    pid = os.fork()
    if pid > 0:
        print(f" Soy el proceso padre. PID hijo:{pid}")
    else:
        print(f" Soy el proceso hijo. PID: {os.getppid()}, PID padre: {os.getppid()}")
    
creo_proceso()

