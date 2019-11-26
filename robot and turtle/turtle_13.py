from turtle import *
from math import *

def circle(radius):
	for i in range(100):
		forward(radius*2 / 100*pi)
		right(360 / 100)

def halfcircle(radius):
	for i in range(100):
		forward(radius*2 / 100*pi)
		right(180 / 100)

speed(0)

penup()
goto(-300, 0)
left(90)
pendown()
begin_fill()
color('yellow')
circle(300)
end_fill()

penup()
goto(-160, 140)
pendown()
begin_fill()
color('blue')
circle(40)
end_fill()

penup()
goto(110, 140)
pendown()
begin_fill()
color('blue')
circle(40)
end_fill()

penup()
goto(200, -20)
pendown()
right(180)
color('pink')
width(25)
halfcircle(100)

penup()
goto(0, 50)
pendown()
color('brown')
right(180)
forward(70)

done()