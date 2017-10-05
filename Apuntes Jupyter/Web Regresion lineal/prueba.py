from colorama import init, Fore, Back, Style #Libreria de colores y stilos de print
from IPython.display import clear_output
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns
import os
from io import open
b_x = []
b_t = []
def clear(): #Funcion para limpiar las diferentes pantallas
    if os.name == "nt": # Windows
        os.system("cls")
    elif os.name == "posix": # Linux / Mac
        os.system("clear")
    clear_output(wait=True) #Jupyter
def tablaRegistros(): #Funcion para mostrar tabla de registros
            print(Fore.YELLOW+"M²\tPrecio")
            for i in range(len(b_t)):
                print(Fore.GREEN+"{}\t{}".format(b_x[i],b_t[i]))
while(True): #MENU
    print(Fore.CYAN+"\nBienvenido a compucasas.")
    opcion = int(input("""\nMenu, digite un numero:
    1)Deseo ingresar los datos.
    2)Imprimir los datos.
    3)Deseo predecir el valor de una casa.
    4)Graficar el pronostico con histogramas
    5)Graficar el pronostico sin histogramas
    99)Salir\n"""))
    if opcion == 1: #INGRESO DE DATOS
        while(True):
            print(Fore.GREEN+"Registro de datos")
            x = input("Introduzca el numero de m²:\n")
            if x.isdigit() and x != '0':
                b_x.append(float(x))
                clear()
                print(Fore.GREEN+"El valor que introduciste es {}m² \n".format(x))
                break
            else:
                clear()
                print(Fore.RED+"\nEl dato introducido no es un numero o es 0, {}\n".format(x))
        while(True):
            print(Fore.GREEN+"Registro de datos")
            t = input("Introduzca el precio por piso:\n")
            if t.isdigit() and t != '0':
                b_t.append(float(t))
                clear()
                print(Fore.GREEN+"El valor que introduciste es {} Millones \n".format(t))
                break
            else:
                clear()
                print(Fore.RED+"\nEl dato introducido no es un numero o es 0, {}\n".format(t))
        print ("¡Datos registrados!")
    elif opcion == 2: #MUESTRA TABLA DE REGISTROS
        print(Fore.BLUE+"Los datos ingresados son\n")
        tablaRegistros()
        input("Enter para continuar\n")
        clear()
    elif opcion == 3: #PRONOSTICO
        while(True):
            print(Fore.GREEN+'\nPronostico :)')
            f = input("Pronostica el valor del piso para este numero de m²:\n")
            if f.isdigit() and f != '0':
                forecast = float(f)
                clear()
                print(Fore.GREEN+'\nPronostico :)\n')
                #Code forecast(Regresion Lineal)
                #¨x = a + bt    pronostico = punto interseccion + pendiente por valor de cambio
                ##Pendiente
                print("""Resolviendo la pendiente""")
                ###autosuma de x*t
                ####Lambda funcion anonima
                ####Map recibe una funcion, y entrega un iterable de tipo map
                ####list recibe una funcion y entrega una lista
                ####Por ultimo sumo todos los valores de la lista
                plusxFort = sum(list(map(lambda x,y: x*y, b_x,b_t)))
                print("1 - Valor de la suma de todos los elementos de x*t {}".format(plusxFort))
                ###autosuma de t
                plust = sum(b_t)
                print("2 - Valor de la suma de todos los elementos de t {}".format(plust))
                ###autosuma de x
                plusx = sum(b_x)
                print("3 - Valor de la suma de todos los elementos de x {}".format(plusx))
                ###autosuma de lso valores de x elevados al cuadrado
                powx = sum(list(map(lambda x: x**2, b_x)))
                print("4 - Valor de la suma de todos los elementos de x elevados cada uno al cuadrado {}".format(powx))
                ###cuadrado del resultado de la suma de todos los elementos de x
                powplusx = plusx**2
                print("5 - Valor del cuadrado del resultado de la suma de todos los elementos de x {}".format(powplusx))
                ###Sustitucion para la pendiente
                b = ((len(b_t)*plusxFort)-(plust*plusx))/((len(b_t)*powx)-powplusx)
                print("""6 - Sustiyendo para hallar la pendiente:
    ((longitud de los datos t * Valor de la suma de todos los elementos de x*t)-
    (Valor de la suma de todos los elementos de t * Valor de la suma de todos los elementos de x))
    todo esto divido en 
    ((longitud de los datos t * Valor de la suma de todos los elementos de x elevados cada uno al cuadrado)-
    Valor del cuadrado del resultado de la suma de todos los elementos de x)\n
    b = (({}*{})-({}*{}))/(({}*{})-{})
    b = {}""".format(len(b_t),plusxFort,plust,plusx,len(b_t),powx,powplusx,b))
                ##interseccion
                print("""Resolviendo la interseccion(a = ¨x - b¨t)""")
                ####mediat
                meant = plust/len(b_t)
                print("7 - Valor de la media de t {}".format(meant))
                ###mediax
                meanx = plusx/len(b_x)
                print("8 - Valor de la media de x {}".format(meanx))
                ###Sustitucion para la interseccion
                a = meant - (b * meanx)
                print("""9 - Sustituyendo para hallar la interseccion
    interseccion = mediat - pendiente*mediax\n
    a = {}-({}*{})
    a = {}""".format(meant,b,meanx,a))
                ##Pronostico
                result = a + (b*forecast)
                print("""10 - Haciendo el pronostico(Regresion lineal) de {}m²:    
    pronostico = punto interseccion + (pendiente * valor de cambio)
    ¨x = a + bt
    ¨x = {} + ({} * {})
    """.format(forecast,a,b,forecast))
                print(Fore.BLUE+"El precio de una casa con {}m² es {}\n".format(forecast,result))
                b_x.append(float(forecast))
                b_t.append(float(result))
                tablaRegistros()
                input("Enter para continuar\n")
                clear()
                break
            else:
                clear()
                print(Fore.RED+"\nEl dato introducido no es un numero o es 0, {}\n".format(f))
    elif opcion == 4: #Grafica de regresion
        data = open('data.csv', 'w+')
        content = "MetrosCuadrados,Precio\n"
        for i in range(len(b_t)):
            content += "{},{}\n".format(b_x[i],b_t[i])
        data.write(content)
        data.close()
        data = pd.read_csv('data.csv')
        sns.jointplot(x='MetrosCuadrados', y='Precio', data=data, kind='reg', color="g")
    elif opcion == 99: #SALIR
        print (Fore.RED+"Hasta la vista baby. ಠ_ಠ")
        break
    else: #OPCION INCORRECTA
        clear()
        print("Opcion incorrecta, digite otra porfavor.")
