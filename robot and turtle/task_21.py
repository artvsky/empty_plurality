#!/usr/bin/python3

from pyrob.api import *

@task
def task_4_11():
	move_right()
	move_down()
	fill_cell()
	for i in range(1,14):
		for j in range(0,i-1):
			fill_cell()
			move_right()
		for n in range(0,i-1):
			fill_cell()
			move_left()
		move_down()

if __name__ == '__main__':
	run_tasks()