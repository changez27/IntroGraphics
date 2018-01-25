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
		update(80)

ends = []

ends.append(Point(100,100))
ends.append(Point(150,100))
line_DDA(ends)

ends = []

ends.append(Point(100,100))
ends.append(Point(125,75))
line_DDA(ends)
	
ends = []

ends.append(Point(125,75))
ends.append(Point(150,100))
line_DDA(ends)
	
ends = []

ends.append(Point(100,100))
ends.append(Point(100,200))
line_DDA(ends)
	
ends = []

ends.append(Point(100,200))
ends.append(Point(150,200))
line_DDA(ends)
	
ends = []

ends.append(Point(150,100))
ends.append(Point(150,200))
line_DDA(ends)
	
ends = []

ends.append(Point(125,75))
ends.append(Point(200,75))
line_DDA(ends)
	
ends = []

ends.append(Point(200,75))
ends.append(Point(225,100))
line_DDA(ends)
	
ends = []

ends.append(Point(225,100))
ends.append(Point(225,200))
line_DDA(ends)
	
ends = []

ends.append(Point(225,200))
ends.append(Point(150,200))
line_DDA(ends)
	
ends = []

ends.append(Point(150,100))
ends.append(Point(225,100))
line_DDA(ends)
	
	
win.getMouse()
win.close()
