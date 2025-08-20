from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()
        self.middle_line()
        
        
    def update_scoreboard(self):
        self.goto(-100, 200)  
        self.write(f"{self.l_score}", align="center", font=("Arial", 60, "normal"))
        self.goto(100, 200) 
        self.write(f"{self.r_score}", align="center", font=("Arial", 60, "normal"))
        
    def middle_line(self):
        y_cor = 290
        reached = True
        while reached:
            self.goto(0,y_cor)
            self.write("|", align="center", font=("Arial", 18, "bold"))
            y_cor -= 40
            if y_cor < -290:
                reached=False
            
            
            
    def increase_score1(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()
        self.middle_line()
    def increase_score2(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()
        self.middle_line()
        
        
    
        
    