from turtle import *
from turtle import Screen, Turtle


COL = (0.60156, 0, 0.99218)  
TAR = (0.86328, 0.47656, 0.31250)  

screen = Screen()
screen.tracer(False)

WID, HEIG = screen.window_width(), screen.window_height()

delt = [(red - COL[index]) / HEIG for index, red in enumerate(TAR)]

tur = Turtle()
tur.color(COL)

tur.penup()
tur.goto(-WID/2, HEIG/2)
tur.pendown()

direction = 1

for distance, y in enumerate(range(HEIG//2, -HEIG//2, -1)):

    tur.forward(WID * direction)
    tur.color([COL[i] + delta * distance for i, delta in enumerate(delt)])
    tur.sety(y)

    direction *= -1

screen.tracer(True)
screen.exitonclick()
