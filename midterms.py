from turtle import *
import time
penup()
goto(-10,10)
pendown()
speed(10)
bgcolor("#9fede4")
color("black")
pensize(2)
for i in range(10):
    right(90)
    for i in range(9):
        forward(120)
        right(85)
