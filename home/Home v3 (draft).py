from graphics import *
import math
import random

win=GraphWin("Home", 800, 600) # создаёт окно размера 800x600 пикселей

colors=['red','orange','yellow','green','cyan','blue','violet']

def draw_roof(x, y, increase=1, roof_color="#efe3af", has_roof_window1=True, has_roof_edging_w1=True, objectlist): # крыша
	p=Polygon(Point(x-260*increase, y), Point(x, y-300*increase), Point(x+260*increase, y))
	p.setWidth(3)
	p.setFill(roof_color)
	p.draw(win)
	objectlist.append(p)
	if has_roof_window1==True:
		draw_window1(x, y-155*increase, increase, window1_color, objectlist)
		if has_roof_edging_w1==True:
			draw_edging_w1(x, y-155*increase, increase, edging_w1_color, objectlist)

def draw_window1(x, y, increase=1, window1_color="#98daea", objectlist): # верхнее окно
	g=Polygon(Point(x-50*increase, y), Point(x, y-50*increase), Point(x+50*increase, y), Point(x, y+50*increase))
	z=Line(Point(x-50*increase, y), Point(x+50*increase, y))
	b=Line(Point(x, y-50*increase), Point(x, y+50*increase))
	g.setWidth(3)
	z.setWidth(3)
	b.setWidth(3)
	g.setFill(window1_color)
	g.draw(win)
	z.draw(win)
	b.draw(win)
	objectlist.append(g)
	objectlist.append(z)
	objectlist.append(b)

def draw_edging_w1(x, y, increase=1, edging_w1_color="#b77a5d", objectlist): # окантовка верхнего окна
	k=Polygon(Point(x-70*increase, y), Point(x, y-78*increase), Point(x+70*increase, y), Point(x, y+78*increase))
	k.setWidth(3)
	k.setFill(edging_w1_color)
	k.draw(win)
	objectlist.append(k)

def draw_lamp(x, y, increase=1, lamp_color="yellow", objectlist): # фонарь
	o=Circle(Point(x, y), 26*increase)
	o.setWidth(3)
	o.setFill(lamp_color)
	o.draw(win)
	objectlist.append(o)

def draw_window2(x, y, increase=1, color1="#b77a5d", color2="#98daea", color3="#b77a5d", objectlist): # нижнее окно
	q=Rectangle(Point(x-90*increase, y-7*increase), Point(x+90*increase, y+7*increase))
	q.setWidth(3)
	q.setFill(color1)
	w=Rectangle(Point(x-78*increase, y+7*increase), Point(x+78*increase, y+183*increase))
	w.setWidth(3)
	w.setFill(color2)
	e=Rectangle(Point(x-90*increase, y+183*increase), Point(x+90*increase, y+197*increase))
	e.setWidth(3)
	e.setFill(color3)
	t=Line(Point(x-78*increase, y+56*increase), Point(x+78*increase, y+56*increase))
	t.setWidth(3)
	y=Line(Point(x, y+56*increase), Point(x, y+189*increase))
	y.setWidth(3)
	q.draw(win)
	w.draw(win)
	e.draw(win)
	t.draw(win)
	y.draw(win)
	objectlist.append(q)
	objectlist.append(w)
	objectlist.append(e)
	objectlist.append(t)
	objectlist.append(y)

def draw_door(x, y, increase=1, color1="#b77a5d", color2="#880016", color3="#b77a5d", objectlist): # дверь
	u=Rectangle(Point(x, y), Point(x+163*increase, y+13*increase))
	u.setWidth(3)
	u.setFill(color1)
	i=Rectangle(Point(x+11*increase, y+15*increase), Point(x+151*increase, y+218*increase))
	i.setWidth(3)
	i.setFill(color2)
	a=Rectangle(Point(x+120*increase, y+88*increase), Point(x+129*increase, y+136*increase))
	a.setFill(color3)
	a.setWidth(3)
	u.draw(win)
	i.draw(win)
	a.draw(win)
	objectlist.append(u)
	objectlist.append(i)
	objectlist.append(a)

def draw_trumpet(x, y, increase=1, color1="#7f7f7f", color2="#da4800", objectlist): # труба
	s=Rectangle(Point(x, y), Point(x+110*increase, y+29*increase))
	s.setWidth(3)
	s.setFill(color1)
	d=Polygon(Point(x+26*increase, y+192*increase), Point(x+26*increase, y+30*increase),
			Point(x+88*increase, y+30*increase), Point(x+88*increase, y+120*increase))
	d.setWidth(3)
	d.setFill(color2)
	s.draw(win)
	d.draw(win)
	objectlist.append(s)
	objectlist.append(d)

def draw_house(x, y, increase=1, color1="red", color2="blue", color3="green", color4="brown",
			objectlist, bottomRight, topLeft): # дом
	r=Rectangle(Point(x-231*increase, y), Point(x+231*increase, y+308*increase)) # первый этаж
	r.setWidth(3)
	r.setFill(color1)
	r.draw(win)
	objectlist.append(r)
	color='pink'
	draw_roof(x+3*increase, y, increase, roof_color, objectlist)
	draw_lamp(x+116*increase, y+55*increase, increase, lamp_color, objectlist)
	#draw_window1(x*increase, y+20*increase, increase, color, objectlist)
	draw_window2(x-89*increase, y+31*increase, increase, color1, color2, color3, objectlist)
	draw_door(x+30*increase, y+89*increase, increase, color1, color2, color3, objectlist)
	draw_trumpet(x-179*increase, y-315*increase, increase, color1, color2, objectlist)
	bottomRight.x=x+25*increase
	bottomRight.y=y
	topLeft.x=x-34*increase
	topLeft.y=y-100*increase

def draw_tree(x, y, t_i=1, trunk_color="brown", needles_color="green"): 
	# дерево (координаты центра верхней стороны ствола, увеличение, цвет ствола, цвет иголок)
	tree_trunk=Rectangle(Point(x-10*t_i, y), Point(x+10*t_i, y+50*t_i)) # ствол ёлки (контур)
	tree_trunk.setFill(trunk_color)
	christmas_tree_needles=Polygon(Point(x, y), Point(x-45*t_i, y), Point(x-20*t_i, y-30*t_i), Point(x-35*t_i, y-30*t_i),
						Point(x-10*t_i, y-60*t_i), Point(x-25*t_i, y-60*t_i), Point(x,y-90*t_i), Point(x+25*t_i, y-60*t_i),
						Point(x+10*t_i, y-60*t_i), Point(x+35*t_i, y-30*t_i), Point(x+20*t_i, y-30*t_i), Point(x+45*t_i, y))
						# ёлки иголки (контур дерева)
	christmas_tree_needles.setFill(needles_color)
	tree_trunk.draw(win)
	christmas_tree_needles.draw(win)

def draw_sun(x, y, sun_radius, sun_color, sun_increase=1): # солнце (координаты, радиус, цвет, увеличение)
	solar_corona=Circle(Point(x, y), sun_radius*sun_increase)
	solar_corona.setFill(sun_color)
	advertisement_YOTA=Text(Point(x, y), "Реклама YOTA на Солнце")
	solar_corona.draw(win)
	if sun_radius>=95:
		advertisement_YOTA.draw(win)

def draw_cloud(x, y, A, B, cloud_color, c_i=1): # облако (координаты центра, большие оси, цвет, увеличение)
	cloud=Oval(Point(x-A/2*c_i, y-B/2*c_i), Point(x+A/2*c_i, y+B/2*c_i))
	cloud.setFill(cloud_color)
	cloud.draw(win)

def draw_person(x, y, size=1, this_person_is_a_man=True): # человек (координаты центра, размер, пол)
	head=Circle(Point(x, y), 15*size)
	head.setFill("white")
	eye_r=Circle(Point(x-4*size, y-4*size), 1*size)
	eye_l=Circle(Point(x+4*size, y-4*size), 1*size)
	roth=Line(Point(x-4*size, y+4*size), Point(x+4*size, y+4*size))
	head.draw(win)
	eye_r.draw(win)
	eye_l.draw(win)
	roth.draw(win)
	if this_person_is_a_man==True:
		body1=Polygon(Point(x, y+65*size), Point(x-30*size, y+15*size), Point(x+30*size, y+15*size))
		body1.setFill("red")
		body1.draw(win)
		hand_r1=Line(Point(x-30, y+15*size), Point(x-45*size, y+40*size))
		hand_r1.draw(win)
		hand_l1=Line(Point(x+30, y+15*size), Point(x+45*size, y+40*size))
		hand_l1.draw(win)
		leg_r1=Line(Point(x-12*size, y+45*size), Point(x-12*size, y+80*size))
		leg_r1.draw(win)
		leg_l1=Line(Point(x+12*size, y+45*size), Point(x+12*size, y+80*size))
		leg_l1.draw(win)
	if this_person_is_a_man==False:
		body2=Polygon(Point(x, y+15*size), Point(x-30*size, y+65*size), Point(x+30*size, y+65*size))
		body2.setFill("green")
		body2.draw(win)
		hand_r2=Line(Point(x, y+15*size), Point(x-25*size, y+40*size))
		hand_r2.draw(win)
		hand_l2=Line(Point(x, y+15*size), Point(x+25*size, y+40*size))
		hand_l2.draw(win)
		leg_r2=Line(Point(x-10*size, y+65*size), Point(x-10*size, y+95*size))
		leg_r2.draw(win)
		leg_l2=Line(Point(x+10*size, y+65*size), Point(x+10*size, y+95*size))
		leg_l2.draw(win)

objectlist=list()
topLeft=Point(0, 0)
bottomRight=Point(0, 0)

draw_house(324, 355, 0.4, "red", "blue", "green", "brown", objectlist, bottomRight, topLeft)
draw_sun(600, 108, 100, "yellow", 1)
draw_cloud(50, 300, 50, 20, "gray", 1)
draw_person(500, 200, 1)

for i in range(1000):
	draw_tree(rnd(80, 720), rnd(60, 540), 1)
	time.sleep(5)
for i in range(1000):
	draw_tree(rnd(80, 720), rnd(60, 540), 1)
	time.sleep(5)
for i in range(1000):
	draw_tree(rnd(80, 720), rnd(60, 540), 1)
	time.sleep(5)

while True:
	for object in objectlist:
		obj.move(vx1, vy1)
	bottomRight.x+=vx1
	bottomRight.y+=vy1
	topLeft.x+=vx1
	topLeft.y+=vy1
	if topLeft.x <= 0 or bottomRight.x >= 1024:
		vx1=-vx1

	if topLeft1.y <= 0 or bottomRight1.y >= 600:
		vy1=-vy1

win.getMouse()
win.close()