from turtle import *      # Importar las funciones de gráficas 
                          # de tortuga.

fi = 1.618033988749895    # Definir φ (sección de oro).

def espiral(n):
    radio = 10            # Definir radio inicial del primer 
                          # arco.    
    for i in range(n):    # Repetir n veces.
        circle(radio, 90) # Dibujar el arco de un cierto radio 
                          # y 90 grados.
        radio *= fi       # Aumentar radio por el factor φ.

hideturtle()       # Esconder la tortuga.
color('SteelBlue') # Establecer color de la pluma: azul 
                   # metálico.
pensize(20)        # Establecer tamaño de la pluma: 20 pixeles.
speed('fast')   # Establecer velocidad de tortuga: rapida.
setheading(270)    # Apuntar la tortuga hacia el sur.
espiral(8)         # Dibujar espiral de orden 8.
done()             # Evitar que la ventana se cierre 
                   # inmediatamente.