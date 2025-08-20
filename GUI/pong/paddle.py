from turtle import Turtle
UP = 90
DOWN = 270 


class Paddle:
    def __init__(self):
        self.paddle1 = Turtle()
        self.paddle2 = Turtle()
        self.segments2 = []
        self.paddle_player1()
        self.paddle_player2()      

    def paddle_player1(self):
        self.paddle1.shape("square")
        self.paddle1.color("white")
        self.paddle1.shapesize(stretch_len=1, stretch_wid=5)
        self.paddle1.penup()
        self.paddle1.goto(350, 0)
            
    def paddle_player2(self):
        self.paddle2.shape("square")
        self.paddle2.color("white")
        self.paddle2.shapesize(stretch_len=1, stretch_wid=5)
        self.paddle2.penup()
        self.paddle2.goto(-350, 0)
            
    def reset(self):
        self.clear()
        self.paddle_player1()
        self.paddle_player2()
            
    def move_player1_up(self):
        if self.paddle1.ycor() < 250:
            cur_x = self.paddle1.xcor()
            new_y = self.paddle1.ycor() + 30
            self.paddle1.goto(cur_x, new_y)
            
    def move_player1_down(self):
        if self.paddle1.ycor() > -250:
            cur_x = self.paddle1.xcor()
            new_y = self.paddle1.ycor() - 30
            self.paddle1.goto(cur_x, new_y)
        
    
    def move_player2_up(self):
        if self.paddle2.ycor() < 250:
            cur_x = self.paddle2.xcor()
            new_y = self.paddle2.ycor() + 30
            self.paddle2.goto(cur_x, new_y)
            
    def move_player2_down(self):
        if self.paddle2.ycor() > -250:
            cur_x = self.paddle2.xcor()
            new_y = self.paddle2.ycor() - 30
            self.paddle2.goto(cur_x, new_y)
    
    
    
                
            
    
        
    
    
    

    
            

        
    

            
