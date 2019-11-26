from turtle import *

def halfcircle(delta):
	for i in range(100):
		forward(delta)
		right(180 / 100)

left(90)
number_of_loops = 10
for i in range(number_of_loops):
	halfcircle(2.5)
	halfcircle(0.5)

done()