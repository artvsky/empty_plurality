from turtle import *

def circle(r):
	for i in range(r):
		forward(3)
		right(360 / r) 
butterfly = 10
r = 80 
for i in range(1, butterfly+1):
	circle(r)
	right(180)
	if (i % 2) == 0:
		r += 20

done()