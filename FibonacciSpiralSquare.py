from turtle import *

fi = 1.618033988749895

def cuadro(longitud):
    """Dibuja un cuadrado relleno cuyos lados son de tamaño
       'longitud'.
    """
    begin_fill()
    for i in range(4):
        fd(longitud)
        lt(90)
    end_fill()

def rectangulo_dorado(n, longitud):
    """Dibuja un rectángulo dorado compuesto de 'n'
       cuadrados. El primer cuadrado tiene sus lados de
       tamaño 'longitud'.
    """
    for i in range(n):
        cuadro(longitud)

        # Mover la tortuga a la esquina contraria y girarla
        # 90 grados a la izquierda.
        fd(longitud)
        lt(90)
        fd(longitud)

        longitud *= fi

def espiral_dorada(n, radio):
    """Dibuja una espiral dorada compuesta de 'n' arcos. El
       primer arco tiene un radio de tamaño 'radio'.
    """
    for i in range(n):
        circle(radio, 90)
        radio *= fi

def espiral(n, radio):
    """Dibuja una espiral dorada de orden 'n' sobre el
       rectángulo dorado que lo alberga.
       El primer arco/cuadro tiene un radio/lado de tamaño
       'radio'.
    """

    color('White')
    fillcolor('SteelBlue')
    pensize(1)
    rectangulo_dorado(n, radio)

    # Regresa la tortuga al centro de la pantalla pero sin
    # dibujar por su paso.
    penup()
    home()
    pendown()

    color('Gold')
    pensize(4)
    espiral_dorada(n, radio)

hideturtle()
speed('normal')
espiral(11, 2)
done()