from turtle import * 

x1 = 20 
x2 = 30 
for i in range(10): 
	for i in range(4): 
		forward(x1) 
		left(90) 
	penup() 
	right(90) 
	forward(x2) 
	right(90) 
	forward(x2) 
	left(180) 
	pendown() 
	x1 += x2*2