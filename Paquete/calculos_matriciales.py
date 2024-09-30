def sumar_filas_matriz (matriz: list) -> list:
    #Esta funcion suma unicamente las filas de una matriz.
    suma = [0] * len(matriz)
    for i in range (len(matriz)):
        for j in range(len(matriz[i])):
            suma[i] += matriz [i][j]
    return suma

def sumar_columnas_matriz (matriz: list) -> list:
    #Esta funcion suma unicamente las columnas de una matriz.
    suma = [0] * len(matriz[0])
    for i in range (len(matriz)):
        for j in range(len(matriz[i])):
            suma[j] += matriz [i][j]
    return suma

def acumular_matriz (matriz: list) -> int:
    #Esta función suma todos los elementos de una matriz.
    acumulador = 0
    for i in range (len(matriz)):
        for j in range (len(matriz[i])):
            acumulador += matriz[i][j]
    return acumulador