from turtle import *

def nangle(n, side_length):
	for i in range(n):
		left(90 + 180/n)
		forward(side_length)
		right(90 - 180/n)

length_step = 10
side_length = 80
gap = 15
x = 0
y = 0

for i in range(10):
	nangle(i+3, side_length)
	side_length += length_step
	x += gap
	penup()
	goto(x,y)
	pendown()

done()