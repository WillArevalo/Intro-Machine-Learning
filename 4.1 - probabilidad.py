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
    datos.sort()
    if n % 2 == 0: # si es par la formula es: Me = X(n / 2 ) + X((n / 2) + 1)
        mediana = (datos[int((n / 2) + 1) - 1] + datos[int( n / 2)] - 1) / 2
    else: # Si es impar la formula es: Me = X((n + 1) / 2)
        mediana = datos[int((n + 1) / 2) - 1]
    return mediana

def estadisticas(datos):
    print("El promedio es {}".format(promedio(datos)))
    print("La moda es {}".format(moda(datos)))
    print("La mediana es {}".format(mediana(datos)))


estadisticas([1,5,3,8,9,9,10])
