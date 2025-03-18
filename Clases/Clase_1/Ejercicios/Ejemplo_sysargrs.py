# Ejemplo basico (chatgpt)

import sys

print(f"Nombre del script: {sys.argv[0]}")

if len(sys.argv) > 1:
    print(f"Hola, {sys.argv[1]}!")
else:
    print("No proporcionaste un nombre.")

# Lo ejecutas: python3 Ejercicios_sysargrs.py Ignacio (Elijes el nombre)
# Salida: Nombre del script: Ejercicios_sysargrs.py
                            # Hola, Ignacio!