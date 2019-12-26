from graphics import *
import math
import random

"""
    Солнце
    x, y - координаты центра
    radius - радиус
    color - цвет двери
    size - масштаб
    """
def Draw_Sun(x, y, radius, color, size = 1):
    obj = Circle(Point(x, y), radius * size)
    obj.setFill(color)
    obj.draw(win)
    """
    Крыша
    x, y - координаты левого верхнего угла стены
    size - масштаб
    roof_color - цвет крыши
    win_color - цвет окон
    """
def Draw_Roof(x, y, size, roof_color, win_color, objectlist):
    w = 174*size #ширина потолка
    h = 99*size #высота крыши
    obj = Polygon(Point(x - 34*size, y), Point( (x + w/2), y-h) , Point(x + w + 34*size, y))
    obj.setFill(roof_color)
    obj.draw(win)
    objectlist.append(obj)
    obj = Polygon(Point(x, y), Point( (x + w/2), y-h) , Point(x + w, y))
    obj.setFill(roof_color)
    obj.draw(win)
    objectlist.append(obj)    
    Draw_Window1(x + w/3, y - 27*size, 14*size, size, win_color, True, objectlist)
    Draw_Window1(x + w/3*2, y - 27*size, 14*size, size, win_color, True, objectlist)
    """
    Круглое окно на крыше
    x, y - координаты центра окна
    radius - радиус
    size - масштаб
    color - цвет окна
    draw_line - рисовать ли рамы
    """
def Draw_Window1(x, y, radius, size, color, draw_line, objectlist):
    obj = Circle(Point(x, y), radius)
    obj.setFill(color)
    obj.draw(win)
    objectlist.append(obj)
    if draw_line == True:
        line1 = Line(Point(x - radius*2/2, y), Point(x + radius*2/2, y))
        line1.draw(win)
        objectlist.append(line1)
        line2 = Line(Point(x, y - radius*2/2), Point(x, y + radius*2/2))        
        line2.draw(win)
        objectlist.append(line2)
    """
    Прямоугольное окно
    x, y - координаты верхнего левого угла окна
    w, h - ширина и высота
    color - цвет окна
    draw_line - рисовать ли рамы
    """
def Draw_Window2(x, y, w, h, color, draw_line, objectlist):
    obj = Rectangle(Point(x, y), Point(x + w, y + h))
    obj.setFill(color)
    obj.draw(win)
    objectlist.append(obj)
    if draw_line == True:
        line1 = Line(Point(x + w/2, y), Point(x + w/2, y + h))
        line1.draw(win)
        objectlist.append(line1)
        line1 = Line(Point(x + w/2, y + h/4), Point(x + w, y + h/4))
        line1.draw(win)
        objectlist.append(line1)
    """
    Дверь
    x, y - координаты верхнего левого угла
    size - масштаб
    color - цвет двери
    handlePos - местоположение ручки
    """
def Draw_Door(x, y, size, color, handlePos, objectlist):
    w = 32*size #ширина
    h = 66*size #высота 
    obj = Rectangle(Point(x, y), Point(x + w, y + h))
    obj.setFill(color)
    obj.draw(win)
    objectlist.append(obj)
    if (handlePos == "Right"):
        h = Circle(Point(x + w - 5*size, y + h/2), 2*size)
        h.setFill("#008000")
    else:
        h = Circle(Point(x + 5*size, y + h/2), 2*size)
        h.setFill("#008000")
    h.draw(win)
    objectlist.append(h)
    """
    Дом
    x, y - координаты верхнего левого угла стены
    size - масштаб
    house_color  - цвет дома
    roof_color  - цвет крыши
    win1_color  - цвет окон на крыше
    win2_color  - цвет окон в доме
    handlePos - местоположение ручки
    """
def Draw_House(x, y, size, house_color, roof_color, win1_color, win2_color, objectlist, topLeft, bottomRight):
    w = 174*size #ширина
    h = 136*size #высота
    obj = Rectangle(Point(x, y), Point(x + w, y + h))
    obj.setFill(house_color)
    obj.draw(win)
    objectlist.append(obj)
    Draw_Roof(x, y, size, roof_color, win1_color, objectlist)
    Draw_Window2(x + 21*size, y + 18*size, 61*size, 31*size, win2_color, False, objectlist )
    Draw_Window2(x + 112*size, y + 18*size, 43*size, 19*size, win2_color, False, objectlist )
    Draw_Window2(x + 21*size, y + 68*size, 62*size, 48*size, win2_color, True, objectlist )
    Draw_Door(x + 118*size, y + 68*size, size, "#ff8040", "Right", objectlist)
    topLeft.x = x - 34*size
    topLeft.y = y - 99*size
    bottomRight.x = x + w + 34*size
    bottomRight.y = y + h;    
    """
    Облако
    x, y - координаты центра
    h, w - высота, ширина
    color - цвет
    size - масштаб
    """
def Draw_Cloud(x, y, h, w, color, size = 1):
    obj = Oval(Point(x - w/2*size, y - h/2*size ), Point(x + w/2*size, y + h/2*size))
    obj.setFill(color)
    obj.draw(win)
    """
    Дерево
    x, y - координаты верхнего левого угла ствола
    radius - радиус кроны
    size - масштаб
    """
def Draw_Tree(x, y, radius, size = 1):
    obj = Rectangle(Point(x, y), Point(x + 20*size, y + 130*size))
    obj.setFill("brown")
    obj.draw(win)
    obj = Circle(Point(x + 10*size, y), radius * size)
    obj.setFill("green")
    obj.draw(win)
    """
    Ребенок
    x, y - координаты центра головы
    size - масштаб
    """
def Draw_Child(x, y, size = 1):
    obj = Circle(Point(x, y), 20*size)
    obj.setFill("white")
    obj.draw(win)
    obj = Polygon(Point(x, y + 20*size), Point(x - 40*size, y + 80*size), Point(x + 40*size, y + 80*size))
    obj.setFill("red")
    obj.draw(win)
    obj = Line(Point(x, y + 20*size), Point(x + 40*size, y + 60*size))
    obj.draw(win)
    obj = Line(Point(x, y + 20*size), Point(x - 40*size, y + 60*size))
    obj.draw(win)
    obj = Line(Point(x - 10*size, y + 80*size), Point(x - 10*size, y + 110*size))
    obj.draw(win)
    obj = Line(Point(x + 10*size, y + 80*size), Point(x + 10*size, y + 110*size))
    obj.draw(win)


#######################################################################################################
win = GraphWin("Home2D", 800, 600)

objlist1 = list()
objlist2 = list()
topLeft1 = Point(0, 0)
bottomRight1 = Point(0, 0)
topLeft2 = Point(0, 0)
bottomRight2 = Point(0, 0)
colors = ('blue', 'lightblue', 'green', 'cyan', 'red', 'purple', 'yellow', 'white', 'grey', 'brown')

Draw_Cloud(200, 50, 20, 50, "lightblue",1)
Draw_Cloud(300, 50, 20, 50, "lightblue", 2)
Draw_Sun(568, 68, 32, "#ffff00", 1.5)
Draw_Tree(650, 300, 50, 1.5)
Draw_Child(100, 400, 1)

size1 = 1
size2 = 0.5
x1 = 300
y1 = 200
x2 = 50
y2 = 250
Draw_House(x1, y1, size1, colors[random.randrange(0, len(colors), 1)] , "#008080", "#00ffff", "#0080ff", objlist1, topLeft1, bottomRight1)
Draw_House(x2, y2, size2, colors[random.randrange(0, len(colors), 1)] , "#008080", "#00ffff", "#0080ff", objlist2, topLeft2, bottomRight2)

dx1 = 1
dy1 = 1
dx2 = 0.5
dy2 = 0.5

while True:
    for obj in objlist1:
        obj.move(dx1, dy1)
        
    topLeft1.x+=dx1        
    topLeft1.y+=dy1
    bottomRight1.x+=dx1
    bottomRight1.y+=dy1        

    for obj in objlist2:
        obj.move(dx2, dy2)
        
    topLeft2.x+=dx2        
    topLeft2.y+=dy2
    bottomRight2.x+=dx2
    bottomRight2.y+=dy2
            
    time.sleep(0.0001)

    if topLeft1.x <= 0 or bottomRight1.x >= 800:
        dx1*=-1
        objlist1[0].setFill(colors[random.randrange(0, len(colors), 1)])

    if topLeft1.y <= 0 or bottomRight1.y >= 600:
        dy1*=-1
        objlist1[0].setFill(colors[random.randrange(0, len(colors), 1)])

    if topLeft2.x <= 0 or bottomRight2.x >= 800:
        dx2*=-1
        objlist2[0].setFill(colors[random.randrange(0, len(colors), 1)])

    if topLeft2.y <= 0 or bottomRight2.y >= 600:
        dy2*=-1
        objlist2[0].setFill(colors[random.randrange(0, len(colors), 1)])

    if (
        (topLeft2.x >= topLeft1.x and topLeft2.x <= bottomRight1.x and topLeft2.y >= topLeft1.y  and  topLeft2.y <= bottomRight1.y) or 
        (bottomRight2.x >= topLeft1.x and bottomRight2.x <= bottomRight1.x and bottomRight2.y >= topLeft1.y  and  bottomRight2.y <= bottomRight1.y) or
        (bottomRight2.x >= topLeft1.x and bottomRight2.x <= bottomRight1.x and bottomRight2.y >= topLeft1.y  and  bottomRight2.y <= bottomRight1.y) or
        (topLeft2.x >= topLeft1.x and topLeft2.x <= bottomRight1.x and bottomRight2.y >= topLeft1.y  and  bottomRight2.y <= bottomRight1.y)
        ):
        dy2*=-1
        dy1*=-1
        dx2*=-1
        dx1*=-1
        objlist1[0].setFill(colors[random.randrange(0, len(colors), 1)])
        objlist2[0].setFill(colors[random.randrange(0, len(colors), 1)])    

win.getMouse()  
win.close()

