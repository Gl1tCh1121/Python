from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.shape("turtle")
        self.speed("fastest")
        self.setheading(90)
        self.goto(0, -270)        
        
        
    def move(self):
        if self.ycor() < FINISH_LINE_Y:
            self.forward(MOVE_DISTANCE)
            
    def next_level(self):
        self.goto(0, -270)        
        
