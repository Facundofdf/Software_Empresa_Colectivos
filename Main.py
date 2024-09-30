from os import system
system ("cls")

from Paquete.inputs_grales import *
from Paquete.inputs_specifcas import *
from Paquete.validacion_grales import *
from Paquete.calculos_matriciales import *
from Paquete.especificas import *



matriz_recaudaciones = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
lista_legajos = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

flag_menu = True
numero_ingresados = True

while (flag_menu == True):
    opciones = input ("¡Bienvenido!\n1.Cargar planilla: \n2.Mostrar la recaudación de cada coche y línea: \n3.Calcular y mostrar recaudación por línea: \n4.Calcular y mostrar recaudación por coche: \n5.Calcular y mostrar la recaudación total: \n6.Salir.\nElija una opcion: ")
    match opciones:
        case "1":
            print("Cargar planilla: ")
            legajo = get_int ("Legajo: ")
            legajo = validacion_int(legajo, "Invalido.",1,15)
            datos = cargar_datos_matriz(matriz_recaudaciones)
            numero_ingresados = False
        case "2":
            if (numero_ingresados == False):
                print("Mostrar la recaudación de cada coche y línea: ")
                mostrar_recaudacion = mostrar_matriz(matriz_recaudaciones)
                print(mostrar_recaudacion)
        case "3":
            if (numero_ingresados == False):
                print("Calcular y mostrar recaudación por línea: ")
                recaudacion_por_linea = sumar_filas_matriz(matriz_recaudaciones)
                for i in range (len(recaudacion_por_linea)):
                    print(f"Linea {i+1}: {recaudacion_por_linea[i]}")
        case "4":
            if (numero_ingresados == False):
                print("Calcular y mostrar recaudación por coche: ")
                recaudacion_por_coche = sumar_columnas_matriz(matriz_recaudaciones)
                for i in range (len(recaudacion_por_coche)):
                    print(f"Coche {i+1}: {recaudacion_por_coche[i]}")
        case "5":
            if (numero_ingresados == False):
                print("Calcular y mostrar la recaudación total: ")
                recaudacion_total = acumular_matriz(matriz_recaudaciones)
                print(f"La recaudación total es: {recaudacion_total}")
        case "6":
            print("Gracias por nuestra app.")
            flag_menu = False
        case _:
            print("No elijio una opcion valida.")
    system("pause")