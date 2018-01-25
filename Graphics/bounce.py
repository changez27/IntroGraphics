from graphics import *
import random

win = GraphWin("Bounce ball",500,500)

def bar1():
    x = random.random()*420
    rect = Rectangle(Point(x,0),Point(x+80,20))
    rect.setFill('red')
    rect.draw(win)
    return Point(x+40,20)

def bar2():
    x = random.random()*420
    rect = Rectangle(Point(x,win.getHeight()),Point(x+80,win.getHeight()-20))
    rect.setFill('red')
    rect.draw(win)
    return Point(x+40,win.getHeight()-20)

cir = Circle(Point(150,150),25)
cir.setFill('yellow')
cir.draw(win)
cent = cir.getCenter()
print (cent)

def line_DDA (cent):
    p1 = bar1()
    p2 = bar2()
    print (p1,p2)
    x = cent.getX()
    y = cent.getY()
    dx = p2.getX() - cent.getX()
    dy = p2.getY() - cent.getY()
    list = []
    x = int(x+0.5)
    y = int(y+0.5)
    if abs(dx) > abs(dy) :
        steps = abs(dx)
    else :
        steps = abs(dy)
        
    Xinc = dx/steps
    Yinc = dy/steps
    
    list.append(Point(x,y))
    step = (int)(steps)
    while int(y) != (int(p2.getY())-25) :
        x1, x = int(x+Xinc)-int(x), x+Xinc
        y1, y = int(y+Yinc)-int(y), y+Yinc
        list.append(Point(x1,y1))
        
    return list

list = line_DDA(cent)
for i in range(len(list)) :
    cir.move(list[i].getX(), list[i].getY())
    cent = cir.getCenter()
    update(30)

win.getMouse()
win.close()