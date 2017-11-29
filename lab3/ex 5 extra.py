from turtle import *
import random
import turtle
colormode(255)

class Rectangle (Turtle):
	def __init__(self,shape,width,hight):
		Turtle.__init__(self) 
			
	
		register_shape("rectangle",((0,0),(width,0),(width,hight),(0,hight)))
		self.shape("rectangle")
	def random_color(self,color):
		self.color(color)
	def random_color(self):
	    r = random.randint(0,256)
	    g = random.randint(0,256)
	    b = random.randint(0,256)
	    self.color((r,g,b))
rectangle1 = Rectangle(50,70,30)
rectangle1.random_color()


mainloop()