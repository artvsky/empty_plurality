from turtle import *
def circle():
	for i in range(100):
		forward(4)
		right(360 / 100)
n = 5
for i in range (n): 
	circle() 
	right(360/n) 

done()