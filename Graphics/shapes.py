from graphics import *

win = GraphWin('Face', 500, 500)

win.plot(100,100,'black')
win.plotPixel(150, 150, 'red')

win.setBackground('sky blue')
print (win.getWidth())
print (win.getHeight())
 
img = Image(Point(350,100), "C:/Users/Prateek.DESKTOP-BIK3U55.000/Downloads/wallpaper5.ppm")
print (img.getHeight())
print (img.getWidth())
img.draw(win)

cir = Circle(Point(250,250),50)
cir.setFill('green')
cir.setWidth(3)
cir.draw(win)

rec = Rectangle(Point(30,20),Point(100,80))
rec.setOutline('blue')
rec.setFill('cyan')
print (rec.getP1(),rec.getP2())
rec.draw(win)

line = Line(Point(50,150),Point(60,250))
line.setArrow('both')
line.draw(win)

msge = Text(Point(100,100), "Hallooo!!!")
msge.setStyle("bold")
msge.setSize(32)
msge.setTextColor("red")
msge.draw(win)

clk = win.getMouse()
print (clk)

win.close()