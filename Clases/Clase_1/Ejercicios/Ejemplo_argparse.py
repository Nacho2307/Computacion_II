# Ejemplo dado por chatgpt

import argparse

def main():
    parser = argparse.ArgumentParser(description="Procesa archivos de entrada y salida.")
    
    # Argumento obligatorio (archivo de entrada)
    parser.add_argument("entrada", help="Archivo de entrada")

    # Argumento opcional con valor
    parser.add_argument("-o", "--output", default="salida.txt", help="Archivo de salida (por defecto: salida.txt)")

    # Flag (sin valor)
    parser.add_argument("-v", "--verbose", action="store_true", help="Modo detallado")

    args = parser.parse_args()

    print(f"Procesando el archivo: {args.entrada}")
    print(f"Archivo de salida: {args.output}")

    if args.verbose:
        print("Modo detallado activado.")

if __name__ == "__main__":
    main()
