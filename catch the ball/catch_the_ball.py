from tkinter import *
from random import randrange as rnd, choice
import math

print('Write your nickname:')
name=input()

colors=['red','orange','yellow','green','cyan','blue','violet']

n=6

class Ball:
	def __init__(self, canvas, x0, y0, x, y, r, v, a, kf=0, flag=0):
		self.x=x
		self.x0=x0
		self.y=y
		self.y0=y0
		self.r=r
		self.v=v
		self.a=a
		self.kf=kf
		self.flag=flag
		self.canvas=canvas
		self.ball=canvas.create_oval(x-r, y-r, x+r, y+r, fill=choice(colors), width=0)
	def kill(self):
		self.kf=1
		canv.delete(self.ball)

root=Tk()
w=root.winfo_screenwidth()//2-400 # устанавливает координату верхнего левого угла окна с учётом размера монитора
h=root.winfo_screenheight()//2-350
root.geometry("800x650+{}+{}".format(w, h))

# задание переменных для подсчёта очков и объектов для отображения счёта очков
count=0
cou=Label(root, font=("Comic Sans MS", 24, "bold"))
cou.place(x=0.5, y=0.5)
cou['text']=count
cou.pack()

# создание холста
canv=Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

balls_list=[]

def create_balls(): # метод создания n шаров и добавления в массив
	for i in range(n):
		# выбор рандомных значений атрибутов шаров
		x=x0=rnd(100, 700)
		y=y0=rnd(100, 500)
		r=rnd(30, 50)
		a=rnd(0, int(2*math.pi*100000))
		v=rnd(100, 500)
		balls_list.append(Ball(canv, x0, y0, x, y, r, v, a))
		move_ball(i)

def new_ball(i): # метод создания шаров, которые идут на замену i элемента в массив
	# выбор рандомных значений атрибутов шаров
	x=x0=rnd(100, 700)
	y=y0=rnd(100, 500)
	r=rnd(30, 50)
	a=rnd(0, int(2*math.pi*100000))
	v=rnd(100, 500)
	balls_list[i]=Ball(canv, x0, y0, x, y, r, v, a)
	move_ball(i)

def move_ball(i): # метод движения шаров
	if balls_list[i].kf!=1:
		balls_list[i].flag+=1
		dx=dy=0
		dx=balls_list[i].v*math.cos(balls_list[i].a/100000)/100
		dy=-balls_list[i].v*math.sin(balls_list[i].a/100000)/100
		balls_list[i].x+=dx
		balls_list[i].y+=dy
		canv.move(balls_list[i].ball, dx, dy)
		rebound_ball(i)
		root.after(10, move_ball, i)
	else:
		new_ball(i)

def rebound_ball(i): # метод отскока шара
	if (balls_list[i].x-balls_list[i].r<=2) or (800-(balls_list[i].x+balls_list[i].r)<=2):
		balls_list[i].a=100000*(math.pi-balls_list[i].a/100000)
	if (balls_list[i].y-balls_list[i].r<=2) or (600-(balls_list[i].y+balls_list[i].r)<=2):
		balls_list[i].a=100000*(2*math.pi-balls_list[i].a/100000)

def click(event): # функция обработки события нажатия на левую кнопку мыши
	for i in range(n):
		if ((event.x-balls_list[i].x)**2 + (event.y-balls_list[i].y)**2) <= balls_list[i].r**2 and balls_list[i].kf!=1:
			global count
			count+=1
			cou['text']=count # счётчик нажатий на шарики
			balls_list[i].kill() # метод ball, который отмечает, что шарик "убит"
			new_ball(i)

canv.bind('<Button-1>', click)
create_balls()
root.mainloop()

f=open('results.txt', 'a')
f.write(name +" "+str(count)+"\n")
f.close()