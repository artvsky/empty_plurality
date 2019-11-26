#!/usr/bin/python3

from pyrob.api import *

@task
def task_8_28():
	while not wall_is_on_the_right():
		move_right()
	while wall_is_above() and wall_is_beneath():
		move_left()
	if not wall_is_above():
		while not wall_is_above():
			move_up()
		while not wall_is_on_the_left():
			move_left()
	else:
		while not wall_is_beneath():
			move_down()
		while not wall_is_on_the_left():
			move_left()
		while not wall_is_on_the_right():
			move_up()

if __name__ == '__main__':
	run_tasks()