from graphics import *

win = GraphWin('temp',500,500)

line = Line(Point(50,50),Point(100,100))

for i in range(10) :
    line.move(120+i, 100+i)
    line.draw(win)  


win.getMouse()
win.close()