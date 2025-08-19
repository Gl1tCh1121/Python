# from turtle import Turtle, Screen

# tim = Turtle()

## square

# tim.color("red")
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)

## DASHED LINES

# for _ in range(10): 
#     tim.forward(10)  
#     tim.penup()      
#     tim.forward(10)  
#     tim.pendown()




# for _ in range(3):
#     tim.color("red")
#     tim.forward(100)
#     tim.right(120)
# for _ in range(4):
#     tim.color("blue")
#     tim.forward(100)
#     tim.right(90)
# for _ in range(5):
#     tim.color("yellow")
#     tim.forward(100)
#     tim.right(72)
# for _ in range(6):
#     tim.color("green")
#     tim.forward(100)
#     tim.right(60) 
# for _ in range(8):
#     tim.color("black")
#     tim.forward(100)
#     tim.right(45) 
# for _ in range(10):
#     tim.color("purple")
#     tim.forward(100)
#     tim.right(36)
# 
# import random as rand
# from turtle import Turtle, Screen
# tim = Turtle()
# # tim.shape("turtle")
# tim.speed(10)
# tim.pensize(5)
# screen = Screen()
# screen.colormode(255)

# colours = ["black","purple", "green","yellow","blue","red"]
# direction = [1, 2]
# while 2*2==4:
#     r = rand.randint(0, 255)  
#     g = rand.randint(0, 255) 
#     b = rand.randint(0, 255)  
#     tim.color(r, g, b)
#     tim.forward(30)
#     if rand.choice(direction) == 1:
#         tim.left(90)
#     else:
#         tim.right(90)
    
# screen.exitonclick()

import random as rand
from turtle import Turtle, Screen

screen = Screen()
screen.colormode(255)
tim = Turtle()
tim.speed(0)  
tim.pensize(1)

for _ in range(120):
    r = rand.randint(0, 255)  
    g = rand.randint(0, 255) 
    b = rand.randint(0, 255)  
    tim.color(r, g, b)
    tim.circle(100)
    tim.right(3)


screen.exitonclick()