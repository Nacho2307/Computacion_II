import argparse

parser = argparse.ArgumentParser(description="Un script básico para procesar archivos.")

parser.add_argument("entrada", help="El archivo de entrada (obligatorio)")

parser.add_argument("-o", "--salida", default="resultado.txt", help="El archivo de salida (opcional)")

parser.add_argument("-v", "--verbose", action="store_true", help="Activar modo detallado")

args = parser.parse_args()

print(f"Archivo de entrada: {args.entrada}")
print(f"Archivo de salida: {args.salida}")

if args.verbose:
    print("Modo detallado: ¡Activado!")

