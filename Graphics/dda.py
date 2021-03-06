from graphics import *
 
win = GraphWin("DDA",500,500)

def round(a):
	return (int)(a+0.5)

def line_DDA (ends):
	x = ends[0].getX()
	y = ends[0].getY()
	dx = ends[1].getX() - ends[0].getX()
	dy = ends[1].getY() - ends[0].getY()
	
	x = round(x)
	y = round(y)
	if abs(dx) > abs(dy) :
		steps = abs(dx)
	else :
		steps = abs(dy)
		
	Xinc = dx/steps
	Yinc = dy/steps
	
	win.plotPixel(x,y,"RED")
	step = (int)(steps)
	for k in range(0,step):
		x = x+Xinc
		y = y+Yinc
		win.plotPixel(x,y,"RED")
		
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

