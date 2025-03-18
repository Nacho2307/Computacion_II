# Ejemplo dado por chatgpt

import sys
import getopt

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "ho:v", ["help", "output="])
    except getopt.GetoptError as err:
        print(err)
        sys.exit(2)

    output_file = None

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print("Uso: script.py -o <archivo>")
            sys.exit()
        elif opt in ("-o", "--output"):
            output_file = arg
        elif opt == "-v":
            print("Versión 1.0")
            sys.exit()

    print(f"Archivo de salida: {output_file}")

if __name__== "__main__":
    main()

