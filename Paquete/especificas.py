def mostrar_matriz (matriz: list) -> None:
    #Esta funcion muestra una matriz indicando las lineas en las filas y los coches en las columnas.
    print("--------",end="\t")
    for j in range (len(matriz[0])):
        print(f"Coche {j+1}", end="\t")
    print("")
    for i in range (len(matriz)):
        print(f"Linea {i+1}:",end="\t")
        for j in range (len(matriz[i])):
            print(matriz[i][j], end="\t")
        print("")