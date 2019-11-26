from turtle import *

n = 100 
left(90) 
penup() 
forward(40) 
pendown() 
right(90) 
for i in range(n): 
	forward(3) 
	right(360/n)

done()