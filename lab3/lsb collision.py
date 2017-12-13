from turtle import *
import random
class Ball(Turtle):
	def __init__(self,radius,color,speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.speed(speed)
Ball1= Ball(20,"blue",40)
Ball2 = Ball (30,"RED",40)
Ball1.goto(100,100)
Ball2.goto(-100,100)

def check_collision(ball1,ball2):ball2.xcor()

	r1=ball1.radius
	r2=ball2.radius
	x1=ball1.xcor()
	x2=ball2.xcor()
	
mainloop()

