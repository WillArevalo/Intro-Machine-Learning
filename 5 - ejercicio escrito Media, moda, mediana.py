#
#Éste es el ejercicio que te ayudará a repasar los conceptos básicos que hemos visto de Probabilidad y Estadística:
#
#Encontrar la Media de la siguiente serie de números:
#1525, 257, 378, 9543, 7854, 152
#
#Encontrar la Moda de la siguiente serie de números:
#9, 5, 9, 4, 3, 6, 7, 1, 2, 3, 9, 1, 2
#
#Encontrar la Mediana en la siguiente serie de datos, recuerda primero ordenar los números de menor a mayor:
#8, 5, 9, 4, 3, 6, 7, 1, 2, 3, 9, 1, 2
#
#No olvides compartir los resultados en el sistema de discusiones.
#


#Obtener promedio: promedio([1,5,3,8,9,10])
def promedio(datos):
    print("""Promedio:
Los datos ingresados son {}""".format(datos))
    sumatoria = sum(datos)
    print("La sumatoria da {}".format(sumatoria))
    n = len(datos)
    print("La cantidad de datos es {}".format(n))
    result = sumatoria / n
    return result

#Obtener moda
def moda(datos):
    print("Moda:")
    #Valores a tomar en cuenta
    resultados = []
    repeticiones = 0
    #Contar los valores y obtener los mas repetidos
    for i in datos:
        apariciones = datos.count(i)
        if apariciones >= repeticiones:
            if apariciones == repeticiones and resultados.count(i) == 0:
                resultados.append(i)
            elif resultados.count(i) == 0:
                resultados = [i]
            repeticiones = datos.count(i)
    return resultados


#Obtener mediana
def mediana(datos):
    print("Mediana:")
    mediana = 0
    n = len(datos)
    datos.sort() #Organiza la lista de menor a mayor
    if n % 2 == 0: # si es par la formula es: Me = X(n / 2 ) + X((n / 2) + 1)
        mediana = (datos[int((n / 2) + 1) - 1] + datos[int( n / 2)] - 1) / 2
    else: # Si es impar la formula es: Me = X((n + 1) / 2)
        mediana = datos[int((n + 1) / 2) - 1]
    return mediana

def estadisticas(datos):
    print("El promedio es {}".format(promedio(datos)))
    print("La moda es {}".format(moda(datos)))
    print("La mediana es {}".format(mediana(datos)))


estadisticas([1525, 257, 378, 9543, 7854, 152])
estadisticas([9, 5, 9, 4, 3, 6, 7, 1, 2, 3, 9, 1, 2])
estadisticas([8, 5, 9, 4, 3, 6, 7, 1, 2, 3, 9, 1, 2])
