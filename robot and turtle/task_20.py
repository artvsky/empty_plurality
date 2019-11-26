#!/usr/bin/python3

from pyrob.api import *


@task
def task_4_3():
    for i in range(12):
        move_right()
        while not wall_is_on_the_right():
            fill_cell()
            move_right()
        while not wall_is_on_the_left():
            move_left()
        move_down()
    move_right()

if __name__ == '__main__':
    run_tasks()