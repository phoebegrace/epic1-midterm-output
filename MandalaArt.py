from turtle import *
import time

bgcolor("white")
title("MandalaArt_Midterms_PhoebeGraceJuayong")

penup()
pensize(3)
speed(30)
begin_fill
for i in range (60):
        penup()
        goto(-12,-26)
        right(102)
        forward(200)
        pendown()
        circle(20)
end_fill

penup()
pensize(1.4)
speed(30)
begin_fill
for i in range (60):
        penup()
        goto(-12,-26)
        right(102)
        forward(170)
        pendown()
        circle(15)
end_fill

penup()
pensize(2)
goto (-10,-195)
speed(20)
begin_fill
for i in range (1):
        penup()
        pendown()
        circle(170)
end_fill

penup()
pensize(2)
goto (-10,-175)
speed(20)
begin_fill
for i in range (1):
        penup()
        pendown()
        circle(150)
end_fill

penup()
pensize(2)
goto (-10,-155)
speed(20)
begin_fill
for i in range (1):
        penup()
        pendown()
        circle(130)
end_fill

up()
pensize(2)
goto(-10,-25)
down()
for j in range(10):
	begin_fill()
	color('black')
	right(360/10)
	for i in range(4):
		forward(105)
		left(90)
	end_fill()

up()
goto(-10, -135)
down()
color("black")
fillcolor("white")
begin_fill()
circle(110)
end_fill()


penup()
goto(-10,0)
pendown()
color("black")
pensize(2)
for i in range(10):
    right(90)
    for i in range(9):
        forward(80)
        right(85)
pendown()
end_fill
