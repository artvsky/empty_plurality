#!/usr/bin/python3

from pyrob.api import *

@task
def task_8_11():
	while not wall_is_on_the_right():
		if wall_is_above() and wall_is_beneath():
			fill_cell()
			move_right()
		elif not wall_is_above() and not wall_is_beneath():
			move_up()
			fill_cell()
			move_down()
			move_down()
			fill_cell()
			move_up()
			move_right()
		elif not wall_is_above():
			move_up()
			fill_cell()
			move_down()
			move_right()
		else:
			move_down()
			fill_cell()
			move_up()
			move_right()
	if wall_is_above() and wall_is_beneath():
		fill_cell()
		move_left()
		move_right()
	elif not wall_is_above() and not wall_is_beneath():
		move_up()
		fill_cell()
		move_down()
		move_down()
		fill_cell()
		move_up()
	elif not wall_is_above():
		move_up()
		fill_cell()
		move_down()
	else:
		move_down()
		fill_cell()
		move_up()

if __name__ == '__main__':
	run_tasks()