# respuesta: hazte con todos pokemon
from huffman import *

def main():
    caracteres = [',','K','Z', 'D', 'C', 'N', 'M', 'P', 'S', 'H', 'E', 'A', 'O', 'T']
    frecuencia = [0.03, 0.03, 0.04, 0.05, 0.06, 0.06, 0.07, 0.07, 0.07, 0.09, 0.1, 0.12, 0.15, 0.15]

    decodificador = crearDecodificador(caracteres, frecuencia)
    print(decodificar(decodificador,'1110001111101100000110001001010101011001101011111110110010110010001010110100001111010101'))

if __name__ == "__main__":
    main()