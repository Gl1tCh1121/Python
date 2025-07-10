from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("white")
        self.speed("fastest")
        self.dx = 10 
        self.dy = 10  
        self.refresh()


    def move(self):
        new_x = self.xcor() + self.dx
        new_y = self.ycor() + self.dy
        self.goto(new_x, new_y)

    def bounce_wall(self):
        self.dy *= -1

    def bounce_paddle(self):
        self.dx *= -1.1
        
    def refresh(self):
        self.goto(0, 0)
        self.dx = 10 
        self.dy = 10 
        self.bounce_paddle() 