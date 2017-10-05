from colorama import init, Fore, Back, Style #Libreria de colores y stilos de print
from IPython.display import clear_output
import os
b_x = []
b_t = []
def clear(): #Funcion para limpiar las diferentes pantallas
    if os.name == "nt": # Windows
        os.system("cls")
    elif os.name == "posix": # Linux / Mac
        os.system("clear")
    clear_output(wait=True) #Jupyter
while(True): #MENU
    print(Fore.CYAN+"\nBienvenido a compucasas.")
    opcion = int(input("""\nMenu, digite un numero:
    1)Deseo ingresar los datos.
    2)Imprimir los datos.
    3)Deseo predecir el valor de una casa.
    99)Salir\n"""))
    if opcion == 1: #INGRESO DE DATOS
        while(True):
            print(Fore.GREEN+"Registro de datos")
            x = input("Introduzca el numero de m²:\n")
            if x.isdigit() and x != '0':
                b_x.append(x)
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
                b_t.append(t)
                clear()
                print(Fore.GREEN+"El valor que introduciste es {} pesos \n".format(t))
                break
            else:
                clear()
                print(Fore.RED+"\nEl dato introducido no es un numero o es 0, {}\n".format(t))
        print ("¡Datos registrados!")
    elif opcion == 2: #MUESTRA TABLA DE REGISTROS
        print(Fore.BLUE+"Los datos ingresados son\n")
        print(Fore.YELLOW+"M²\tPrecio")
        for i in range(len(b_t)):
            print(Fore.GREEN+"{}\t{}".format(b_x[i],b_t[i]))
        input("Enter para continuar\n")
        clear()
    elif opcion == 3: #PRONOSTICO
        while(True):
            print(Fore.GREEN+'\nPronostico :)')
            f = input("Pronostica el valor del piso para este numero de m²:\n")
            if f.isdigit() and f != '0':
                forecast = f
                clear()
                print(Fore.GREEN+"El valor que introduciste es {} \n".format(forecast))
                input("Enter para continuar\n")
                clear()
                break
            else:
                clear()
                print(Fore.RED+"\nEl dato introducido no es un numero o es 0, {}\n".format(f))
    elif opcion == 99: #SALIR
        print (Fore.RED+"Hasta la vista baby. ಠ_ಠ")
        break
    else: #OPCION INCORRECTA
        clear()
        print("Opcion incorrecta, digite otra porfavor.")
        