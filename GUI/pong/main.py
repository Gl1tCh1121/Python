from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle = Paddle()
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(paddle.move_player1_up, "Up")
screen.onkey(paddle.move_player1_down, "Down")
screen.onkey(paddle.move_player2_up, "w")
screen.onkey(paddle.move_player2_down, "s")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()
    
    #det collision with y wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_wall()
        
    #det collision with paddle 
    if paddle.paddle1.distance(ball) < 50 and ball.xcor() > 320:
        ball.bounce_paddle()
    if paddle.paddle2.distance(ball) < 50 and ball.xcor() < -320:
        ball.bounce_paddle()
    
    #det collision with x wall
    if ball.xcor() > 400:
        scoreboard.increase_score1()
        ball.refresh()
        
    elif ball.xcor() < -400:
        scoreboard.increase_score2()
        ball.refresh()
        
        

screen.exitonclick()
