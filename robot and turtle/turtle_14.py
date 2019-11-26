from turtle import * 
from time import * 

speed(0) 

def star(n, length): 
	for i in range(n): 
		forward(length) 
		right(180 - 180/n) 

star(100, 300) 

done()