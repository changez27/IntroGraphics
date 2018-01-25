from graphics import *

win = GraphWin('Circle Mid Pt. Algo',500,500)

def cirmid(pt,r):
	xc = pt.getX()
	yc = pt.getY()
	x = 0
	y = r
	p = 3 - (2*r)
	while x <= y :
		if p < 0 :
			win.plotPixel(x+xc,y+yc,'RED')
			win.plotPixel(-x+xc,y+yc,'RED')
			win.plotPixel(x+xc,-y+yc,'RED')
			win.plotPixel(-x+xc,-y+yc,'RED')
			win.plotPixel(y+xc,x+yc,'RED')
			win.plotPixel(-y+xc,x+yc,'RED')
			win.plotPixel(y+xc,-x+yc,'RED')
			win.plotPixel(-y+xc,-x+yc,'RED')
			p = p + (4*x) + 6
			x = x+1
			y = y
			
		else :
			win.plotPixel(x+xc,y+yc,'RED')
			win.plotPixel(-x+xc,y+yc,'RED')
			win.plotPixel(x+xc,-y+yc,'RED')
			win.plotPixel(-x+xc,-y+yc,'RED')
			win.plotPixel(y+xc,x+yc,'RED')
			win.plotPixel(-y+xc,x+yc,'RED')
			win.plotPixel(y+xc,-x+yc,'RED')
			win.plotPixel(-y+xc,-x+yc,'RED')
			p = p + (4*(x - y)) + 10
			x = x + 1
			y = y - 1
			
		update(25)
		
a = eval(input('Enter Center of Circle: '))
r = eval(input('Enter Radius of circle: '))
pt = Point(a[0],a[1])
cirmid(pt,r)

win.getMouse()
win.close()
