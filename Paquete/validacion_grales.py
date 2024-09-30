def validacion_int (numero:int, mensaje_error:str, minimo:int, maximo:int) -> int:
    #Esta funcion valida un numero entero entre un minimo y un maximo.
    while (numero < minimo or numero > maximo):
        print(mensaje_error)
        numero = int(input("Intentelo nuevamente: "))
    return numero