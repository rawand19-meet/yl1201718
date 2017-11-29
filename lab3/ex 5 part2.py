from turtle import *
register_shape
class Hexagon(Turtle):
	def __init__(self,size):
		Turtle.__init__(self)
		self.shapesize(size)
		self.begin_poly()
		self.penup()
		#turtle.home()

		self.forward(50)
		self.left(60)
		self.forward(50)
		self.left(60)
		self.forward(50)
		self.left(60)
		self.forward(50)
		self.left(60)
		self.forward(50)
		self.left(60)
		self.end_poly()
		p =self.get_poly()
		register_shape("myfaveshape",p)
		self.shape("myfaveshape")
my_hexagon = Hexagon(2)

mainloop()