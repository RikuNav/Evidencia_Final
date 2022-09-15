"""Tic Tac Toe

Exercises

1. Give the X and O a different color and width.
2. What happens when someone taps a taken spot?
3. How would you detect when someone has won?
4. How could you create a computer player?
"""

"""""We import libraries"""
from turtle import update, setup, hideturtle, tracer, onscreenclick, done
from turtle import up, gato, down, circle
from freegames import line


def grid():
    """Draw tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    """Draw X player."""
    line(x, y, x + 133, y + 133)#Diagonal position 1
    line(x, y + 133, x + 133, y)#Diagonal position 2


def drawo(x, y):
    """Draw O player."""
    up()
    goto(x + 67, y + 5)#Position
    down()
    circle(62)#Circle diameter


def floor(value):
    """Round value down to grid with square size 133."""
    return ((value + 200) // 133) * 133 - 200#Size of the square


state = {'player': 0}
players = [drawx, drawo]


def tap(x, y):
    """Draw X or O in tapped square."""
    x = floor(x)
    y = floor(y)
    player = state['player']
    draw = players[player]
    draw(x, y)#Draw the symbol
    update()#Sincronize the trace
    state['player'] = not player#Allows 2 players


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
