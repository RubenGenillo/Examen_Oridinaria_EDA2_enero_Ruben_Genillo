def multiplicar(matriz1, matriz2):
    filas_matriz1 = len(matriz1)
    columnas_matriz1 = len(matriz1[0])
    filas_matriz2 = len(matriz2)
    columnas_matriz2 = len(matriz2[0])
    if columnas_matriz1 != filas_matriz2:
        raise ValueError("Las dimensiones de las matrices no son compatibles para la multiplicación")
    resultado = [[0] * columnas_matriz2 for _ in range(filas_matriz1)]
    for i in range(filas_matriz1):
        for j in range(columnas_matriz2):
            for k in range(filas_matriz2):
                resultado[i][j] += matriz1[i][k] * matriz2[k][j]
    return resultado


def elevar(matriz, n):
    filas = len(matriz)
    columnas = len(matriz[0])
    if n == 0:
        matriz_identidad = [[1 if i == j else 0 for j in range(columnas)] for i in range(filas)]
        return matriz_identidad
    if n == 1:
        return matriz
    matriz_actual = matriz
    resultado = [[1 if i == j else 0 for j in range(columnas)] for i in range(filas)]  # Matriz identidad
    while n > 0:
        if n % 2 == 1:
            resultado = multiplicar(resultado, matriz_actual)
        matriz_actual = multiplicar(matriz_actual, matriz_actual)
        n //= 2

    return resultado


def sumar_listas(listas):
    longitud = len(listas[0])
    if not all(len(lista) == longitud for lista in listas):
        raise ValueError("Todas las listas deben tener la misma longitud")
    resultado = [sum(elementos) for elementos in zip(*listas)]
    return resultado

def teletransportes(M, n):
    matriz = elevar(M, n)
    return sum(sumar_listas(matriz))


if __name__ == "__main__":
    matriz = [[0, 0, 0, 0, 0, 1, 0, 1, 0, 0], [ 0, 0, 0, 0, 0, 0, 1, 0, 1, 0], [ 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],[0, 0, 1, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 1, 0, 0, 1], [0, 1, 0, 0, 0, 1, 0, 0, 0, 0], [1, 0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 1, 0, 0, 0, 0]]
    print(teletransportes(matriz, 1))
    print(teletransportes(matriz, 2))
    print(teletransportes(matriz, 3))
    print(teletransportes(matriz, 5))
    print(teletransportes(matriz, 8))
    print(teletransportes(matriz, 10))
    print(teletransportes(matriz, 15))
    print(teletransportes(matriz, 18))
    print(teletransportes(matriz, 21))
    print(teletransportes(matriz, 23))
    print(teletransportes(matriz, 32))
