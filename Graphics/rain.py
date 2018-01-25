from graphics import *

win = GraphWin('Rain', 500, 500)

line = Line(Point(0,win.getHeight()-100),Point(win.getWidth(),win.getHeight()-100))
line.draw(win)
list = []

for y in range(0,win.getHeight()-100,20):
    x = 0
    for x in range(0,win.getWidth(),20):
        if y<win.getHeight()-100 and y>win.getHeight()-250 and x>175 and x<325 :
            continue
        list.append(Line(Point(x,(y)), Point(x+5,y+10)))

print (list)
p = 0
q = 0

while True :
    for i in range(0,len(list),2):
        if i%2 == 0 :
            list[i].draw(win)
        elif i%3 == 0 :
                list[i].draw(win)
        else :
            continue
        update(9999999999)
    
    for i in range(1,len(list),2):
        if (i-1)%2 == 0 :
            list[i-1].undraw()
        elif (i-1)%3 == 0 :
            list[i-1].undraw()
        else :
            continue
        update(9999999999)
        
clk = win.getMouse()
print (clk)

win.close()