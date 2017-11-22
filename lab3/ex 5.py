from turtle import *
import turtle
import random
turtle.colormode(255)
class Square(Turtle):
	def __init__(self,size):
		Turtle.__init__(self)
		self.shape("square")
		self.shapesize(size)
		
	def random_color(self,color):
		self.color(color)

mysquare=Square(10)
mysquare.random_color((random.randint(0,256),random.randint(0,256),random.randint(0,256)))




mainloop()

