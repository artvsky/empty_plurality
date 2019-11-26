#!/usr/bin/python3

from pyrob.api import *

@task
def task_6_6():
	n=0
	while not wall_is_on_the_right():
		move_right()
		n=n+1
	for i in range(1,n+1):
		if wall_is_above():
			move_left()
		else:
			while not wall_is_above():
				move_up()
				fill_cell()
			while not wall_is_beneath():
				move_down()
			move_left()

if __name__ == '__main__':
	run_tasks()