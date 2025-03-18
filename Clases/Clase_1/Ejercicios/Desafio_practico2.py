# Codigo hecho por mi
'''import argparse

def es_positivo(valor):
    valor = int(valor)
    if valor <= 0:
        raise argparse.ArgumentTypeError("El número debe ser positivo.")
    return valor

parser = argparse.ArgumentParser(description="Un script simple con errores.")

parser.add_argument("-n", "--numero", type=int, required=True, help="Un número entero obligatorio.")
parser.add_argument("-p", "--precio", type=float, help="Un precio en número decimal (opcional).")
parser.add_argument("-l", "--lista", type=int, nargs="+", help="Una lista de enteros.")
parser.add_argument("-x", "--positivo", type=es_positivo, help="Un número positivo validado.")

args = parser.parse_args()

print(f"Número entero (-n): {args.numero}")

if args.precio:
    print(f"Precio decimal (-p): {args.precio}")

if args.lista:
    print(f"Lista de enteros (-l): {args.lista}")

if args.positivo:
    print(f"Número positivo validado (-x): {args.positivo}")'''

# Correcion del codigo con chatgpt

import argparse

def es_positivo(valor):
    valor = int(valor)
    if valor <= 0:
        raise argparse.ArgumentTypeError("El número debe ser positivo.")
    return valor

parser = argparse.ArgumentParser(description="Un script simple y funcional.")

parser.add_argument("-n", "--numero", type=int, required=True, help="Un número entero obligatorio.")
parser.add_argument("-p", "--precio", type=float, help="Un precio en número decimal (opcional).")
parser.add_argument("-l", "--lista", type=int, nargs="+", help="Una lista de enteros.")
parser.add_argument("-x", "--positivo", type=es_positivo, help="Un número positivo validado.")

args = parser.parse_args()

print(f"Número entero (-n): {args.numero}")

if args.precio:
    print(f"Precio decimal (-p): {args.precio}")

if args.lista:
    print(f"Lista de enteros (-l): {args.lista}")

if args.positivo:
    print(f"Número positivo validado (-x): {args.positivo}")
