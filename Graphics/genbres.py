from graphics import *

win = GraphWin("Bresenhams",500,500)

def line_DDA (ends):
	x = ends[0].getX()
	y = ends[0].getY()
	i = 1
	ex_change = 0
	dx = ends[1].getX() - ends[0].getX()
	dy = ends[1].getY() - ends[0].getY()
	sx = dx/abs(dx)
	sy = dy/abs(dy)
	
	if dx < dy :
		dx, dy = dy,dx
		ex_change = 1
	else :
		ex_change = 0
		
	e = (2*dy) - dx
	ddx = int(dx)
	for i in range(0,ddx):
		win.plotPixel(x,y,'RED')
	
		while e >= 0 :
			if (ex_change == 1) :
				x = x+sx
			else :
				y = y+sy
			
			e = e - (2*dy)
			
		if ex_change == 1 :
			y = y+sy
		else :
			x = x+sx
		
		e = e + (2*dy)
			
ends = []
ptx = (eval(input("Enter abscissa of starting point of line:")))
pty = (eval(input("Enter ordinate of starting point of line:")))
pt = Point(ptx,pty)
ends.append(pt)
ptx = (eval(input("Enter abscissa of ending point of line:")))
pty = (eval(input("Enter ordinate of ending point of line:")))
pt = Point(ptx,pty)
ends.append(pt)
line_DDA(ends)

win.getMouse()
win.close()
