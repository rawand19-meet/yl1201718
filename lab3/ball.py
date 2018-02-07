from turtle import *
import turtle

class Ball(Turtle):
	"""docstring for Ball"""
	def __init__(self,x,y,dx,dy,r,color):
		Turtle.__init__(self)
		self.penup()
		
		self.goto(x,y)
		self.dx = dx
		self.dy = dy
		self.r = r
		self.color(color)
		self.shape("circle")
		self.shapesize(r/10)
	def move(self,screen_width,screen_height):
		current_x = self.xcor()
		new_x = current_x + self.dx
	 	current_y = self.ycor()
		new_y = current_y +self.dy

		right_side_ball=new_x+self.r
		left_side_ball=new_x-self.r
		up_side_ball=new_y+self.r
		down_side_ball=new_y-self.r
		self.goto(new_x,new_y)
		self.x = new_x
		self.y = new_y

		self.goto(new_x,new_y)
		if new_x >=screen_width:
			self.dx = -self.dx
		if new_x <= -screen_width:
			self.dx = -self.dx
		if new_y >= screen_height:
			self.dy = -self.dy
		if new_y <= -screen_height:
			self.dy = -self.dy











    




        

        
        
