from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()    
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")




game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    #det collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.add_snake()
        scoreboard.increase_score()
        
    #det collision with wall 
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.game_over()
        game_is_on = False
        
    #det collision with tail 
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

        
    
    
  

    
    









screen.exitonclick()
