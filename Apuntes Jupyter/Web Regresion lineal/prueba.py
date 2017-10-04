from IPython.display import clear_output

while(True):
    print("Bienvenido a compucasas.")
    print("""Menu, digite un numero:
    1)Deseo ingresar los datos.
    2)Deseo predecir el valor de una casa.
    99)Salir""")
    opcion = input()
    clear_output(wait=True)
    b_x = []
    b_t = []
    print(opcion)
    if opcion == '1':
        ipm2 = int(input(print("Introduzca la cantidad de m^2:")))
        b_x.append(ipm2)
        print(b_x)
    if opcion == '99':
        print ("Hasta la vista baby")
        break