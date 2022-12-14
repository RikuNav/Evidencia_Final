"""Pacman, juego clásico de arcade.

Ejercicios

1. Cambiar el tablero.
2. Cambiar el número de fantasmas.
3. Cambiar donde pacman inicia.
4. Hacer que los fantasmas vayan más rápido o lento.
5. Hacer a los fantasmas más inteligentes.
"""


# Librería random, importa choice para
# la selección de un número random
from random import choice

# Librería turtle, que nos ayuda a manipular
# objetos, para que lleven a cabo los movimientos
from turtle import Turtle, bgcolor, clear, \
     up, goto, dot, update, ontimer, setup, hideturtle, \
     tracer, listen, onkey, done

# Librería freegames, que importará floor y vector,
# los cuales,el primero te calcula un punto, desde la izquierda
# dado un valor, o tamaño.
# vector crea objetos de esa clase, con dirección y sentido
from freegames import floor, vector

# Score será el diccionario
state = {'score': 0}
# Estado del camino tanto pintado y sin pintar
path = Turtle(visible=False)
writer = Turtle(visible=False)
# velocidad
aim = vector(5, 0)
# Posición de pacman y fantasmas
pacman = vector(-20, -20)
ghosts = [
    [vector(-180, 160), vector(10, 0)],
    [vector(-180, -140), vector(0, 10)],
    [vector(100, 160), vector(0, -10)],
    [vector(140, -140), vector(-10, 0)],
]
# fmt: off
# Tablero de 20 x 20 (es una matriz de 20 x 20)
# El 1 representa un camino, mientras que los 0 son
# las barreras, que ningun personaje puede llegar
# a atravesar
tiles = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0,
    0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0,
    0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0,
    0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0,
    0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]
# fmt: on

# Función que dibuja el tablero utilizando
# las coordenadas en x y y


def square(x, y):
    """Dibujar cuadrado utilizando path (x, y)."""
    path.up()
    path.goto(x, y)
    path.down()
    path.begin_fill()

    for count in range(4):
        path.forward(20)
        path.left(90)

    # Avanza 20 puntos en el eje
    # Luego se recorre 90 grados a la izquierda
    # Aquí se crea el tablero

    path.end_fill()


def offset(point):
    """Regresar la distancia del punto en cada
    casilla."""
    x = (floor(point.x, 20) + 200) / 20
    y = (180 - floor(point.y, 20)) / 20
    index = int(x + y * 20)
    return index

# Función que revisa si hay caminos
# disponibles para que un fantasma
# pueda moverse


def valid(point):
    """Regresa Verdadero si el punto es
    válido dentro de las casillas."""
    index = offset(point)

    if tiles[index] == 0:
        return False

    index = offset(point + 19)

    if tiles[index] == 0:
        return False

    return point.x % 20 == 0 or point.y % 20 == 0

# Crea realmeente el mundo, y define los colores que
# tendran los caminos y las barreras


def world():
    """Dibujar el mundo utilizando 'path'."""
    bgcolor('black')
    path.color('blue')

    for index in range(len(tiles)):
        tile = tiles[index]

        if tile > 0:
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20
            square(x, y)

            if tile == 1:
                path.up()
                path.goto(x + 10, y + 10)
                path.dot(2, 'white')


def move():
    """Mover a pacman y todos los fantasmas."""
    writer.undo()
    writer.write(state['score'])

    clear()

    # Llama a la función valid(), que validará
    # si el punto al que se planea mover pacman,
    # es disponible o no, si el valor del tile es 0,
    # regresa false y no se moverá, en caso contrario
    # se moverá

    if valid(pacman + aim):
        pacman.move(aim)

    index = offset(pacman)

    # Si offset regresa un índice en el que la posición
    # es 1, el tablero tendrá una posición de 2, volviendose
    # pacman, se aumenta el score
    # Se cambian las coordenadas  y se llamará a la función
    # square() para actualizar la pintura del tablero

    if tiles[index] == 1:
        tiles[index] = 2
        state['score'] += 1
        x = (index % 20) * 20 - 200
        y = 180 - (index // 20) * 20
        square(x, y)

    up()
    goto(pacman.x + 10, pacman.y + 10)
    dot(20, 'yellow')

    for point, course in ghosts:
        if valid(point + course):
            point.move(course)
        else:
            options = [
                vector(10, 0),
                vector(-10, 0),
                vector(0, 10),
                vector(0, -10),
            ]
            plan = choice(options)
            course.x = plan.x
            course.y = plan.y

        up()
        goto(point.x + 10, point.y + 10)
        dot(20, 'red')

    update()

    for point, course in ghosts:
        if abs(pacman - point) < 20:
            return

    ontimer(move, 100)


def change(x, y):
    """Cambiar la dirección de pacman si es válido."""
    if valid(pacman + vector(x, y)):
        aim.x = x
        aim.y = y


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
writer.goto(180, 110)
writer.color('white')
writer.write(state['score'])
listen()

# Va a declarar las teclas que van a llevar a cabo
# el movimiento de pacman

onkey(lambda: change(5, 0), 'Right')
onkey(lambda: change(-5, 0), 'Left')
onkey(lambda: change(0, 5), 'Up')
onkey(lambda: change(0, -5), 'Down')
world()
move()
done()
