from .validacion_grales import validacion_int

def cargar_datos_matriz (matriz: list) -> None:
    #Esta funcion pide la fila y la columna de una matriz, la valida y luego pide el numero a cargar en la matriz.
    linea = int(input("Linea: "))
    linea = validacion_int(linea,"Fuera de rango.",1,3)
    coche = int(input("Coche: "))
    coche = validacion_int(coche,"Fuera de rango.",1,5)
    recaudacion = int(input("Recaudacion: "))
    matriz[linea - 1][coche - 1] += recaudacion