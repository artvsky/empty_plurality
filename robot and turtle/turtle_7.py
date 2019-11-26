from turtle import * 

step = 1 
num_of_rotations = 10 
var = 50 
for i in range(num_of_rotations*var): 
	forward(step) 
	right(360/var) 
	step+=0.02 

done()