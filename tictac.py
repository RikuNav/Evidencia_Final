""" Tic Tac Toe

Exercises

1. Give the X and O a different color and width.
2. What happens when someone taps a taken spot?
3. How would you detect when someone has won?
4. How could you create a computer player?
"""

"""" Import libraries"""
from turtle import up
from turtle import goto
from turtle import down
from turtle import circle
from turtle import update
from turtle import setup
from turtle import hideturtle
from turtle import tracer
from turtle import done
from turtle import color
from turtle import pencolor
from turtle import pensize
from turtle import seth
from turtle import fd
from turtle import Screen
from turtle import mainloop


"""" Define screen setup"""
screen = Screen()
screen.setup(800, 800)
screen.title("Tic Tac Toe")
screen.setworldcoordinates(-5, -5, 5, 5)
screen.bgcolor('light gray')
screen.tracer(0, 0)
hideturtle()


def grid():
    # Set line color to green
    pencolor('green')
    pensize(10)
    up()
    goto(-3, -1)
    seth(0)
    down()
    fd(6)
    up()
    goto(-3, 1)
    seth(0)
    down()
    fd(6)
    up()
    goto(-1, -3)
    seth(90)
    down()
    fd(6)
    up()
    goto(1, -3)
    seth(90)
    down()
    fd(6)


def drawx(x, y):
    """ Draw X player."""
    color('blue')
    up()
    goto(x-0.5, y-0.5)
    down()
    goto(x+0.5, y+0.5)
    up()
    goto(x-0.5, y+0.5)
    down()
    goto(x+0.5, y-0.5)


def drawo(x, y):
    """ Draw O player."""
    up()
    goto(x, y-0.5)
    seth(0)

    # Change color to red
    color('red')
    down()
    circle(0.5, steps=100)


def draw_piece(i, j, p):
    if p == 0:
        return
    x, y = 2*(j - 1), -2*(i - 1)
    if p == 1:
        drawx(x, y)
    else:
        drawo(x, y)


def draw(b):
    # Draw the grid in the user interface
    grid()

    for i in range(3):
        for j in range(3):
            draw_piece(i, j, b[i][j])
    screen.update()


# return 1 if player 1 wins, 2 if player 2 wins, 3 if tie, 0 if game is'nt over
def gameover(b):
    if b[0][0] > 0 and b[0][0] == b[0][1] and b[0][1] == b[0][2]:
        return b[0][0]
    if b[1][0] > 0 and b[1][0] == b[1][1] and b[1][1] == b[1][2]:
        return b[1][0]
    if b[2][0] > 0 and b[2][0] == b[2][1] and b[2][1] == b[2][2]:
        return b[2][0]
    if b[0][0] > 0 and b[0][0] == b[1][0] and b[1][0] == b[2][0]:
        return b[0][0]
    if b[0][1] > 0 and b[0][1] == b[1][1] and b[1][1] == b[2][1]:
        return b[0][1]
    if b[0][2] > 0 and b[0][2] == b[1][2] and b[1][2] == b[2][2]:
        return b[0][2]
    if b[0][0] > 0 and b[0][0] == b[1][1] and b[1][1] == b[2][2]:
        return b[0][0]
    if b[2][0] > 0 and b[2][0] == b[1][1] and b[1][1] == b[0][2]:
        return b[2][0]

    p = 0
    for i in range(3):
        for j in range(3):
            p += (1 if b[i][j] > 0 else 0)
    if p == 9:
        return 3
    else:
        return 0


def play(x, y):
    global turn
    i = 3 - int(y + 5) // 2
    j = int(x + 5) // 2 - 1
    if i > 2 or j > 2 or i < 0 or j < 0 or b[i][j] != 0:
        return
    if turn == 'x':
        b[i][j], turn = 1, 'o'
    else:
        b[i][j], turn = 2, 'x'
    draw(b)
    r = gameover(b)

    # Display notifiacation when the game is over
    if r == 1:
        screen.textinput("Game over!", "X won!")
    elif r == 2:
        screen.textinput("Game over!", "O won!")
    elif r == 3:
        screen.textinput("Game over!", "Tie!")


# Initialize value of matrix

b = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
draw(b)
turn = 'x'
screen.onclick(play)
mainloop()
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
done()
