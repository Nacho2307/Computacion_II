import os

def buscar_zombis():
    print("Buscando procesos zombis en /proc...")
    for pid in [d for d in os.listdir('/proc') if d.isdigit()]:
        try:
            with open(f'/proc/{pid}/status') as f:
                contenido = f.read()
                if 'State:\tZ (zombie)' in contenido:
                    # Extraer información
                    nombre = next(line for line in contenido.split('\n') if line.startswith('Name:'))
                    ppid = next(line for line in contenido.split('\n') if line.startswith('PPid:'))
                    
                    print("Zombi encontrado:")
                    print(f"  PID: {pid}")
                    print(f"  {nombre}")
                    print(f"  {ppid}")
                    print("------------------------")
        except (FileNotFoundError, PermissionError):
            continue
    
    print("Búsqueda completada")

buscar_zombis()