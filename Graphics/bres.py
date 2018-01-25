from graphics import *

win = GraphWin("Bresenhams",500,500)

def line_DDA (ends):
	x = ends[0].getX()
	y = ends[0].getY()
	dx = ends[1].getX() - ends[0].getX()
	dy = ends[1].getY() - ends[0].getY()
	
	win.plotPixel(x,y,'RED')
	
	p = (2*dy) - dx
	ddx = int(dx)
	for k in range(0,ddx):
		if p < 0 :
			x = x+1
			win.plotPixel(x,y,'RED')
			p = p + (2*dy)
		else :
			x = x+1
			y = y+1
			win.plotPixel(x,y,'RED')
			p = p + (2*dy) - (2*dx)
		update(20)

ends = []
ptx = (eval(input("Enter absicca of starting point of line:")))
pty = (eval(input("Enter ordinate of starting point of line:")))
pt = Point(ptx,pty)
ends.append(pt)
ptx = (eval(input("Enter absicca of ending point of line:")))
pty = (eval(input("Enter ordinate of ending point of line:")))
pt = Point(ptx,pty)
ends.append(pt)
line_DDA(ends)

win.getMouse()
win.close()
