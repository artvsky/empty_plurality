#!/usr/bin/python3

from pyrob.api import *

@task
def task_5_10():
	m=1 #для счётчика ширины поля
	n=1 #для счётчика высоты поля
	while not wall_is_on_the_right():
		m=m+1
		fill_cell()
		move_right()
	fill_cell()
	while not wall_is_beneath():
		move_down()
		fill_cell()
		n=n+1
	for i in range(1,m-1):
		if not wall_is_on_the_left():
			move_left()
			fill_cell()
			for i in range(1,n-1):
				move_up()
				fill_cell()
			if wall_is_on_the_left():
				for i in range(1,n-1):
					move_down()
		if not wall_is_on_the_left():
			move_left()
			fill_cell()
			for i in range(1,n-1):
				move_down()
				fill_cell()

if __name__ == '__main__':
	run_tasks()