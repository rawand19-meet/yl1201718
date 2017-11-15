import turtle
turtle.speed(999999)
def drawline():
	turtle.forward(170)
	turtle.right(50)
	turtle.forward(100)
	turtle.right(100)
	turtle.forward(70)
	turtle.home()
for i in range(360):
	turtle.right(i)
	drawline()
turtle.mainloop()