import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move_car()

    #det collision with end wall(next_level) 
    if player.ycor() > 270:
        scoreboard.increase_score()
        player.next_level()
        car_manager.next_level()
        
    #det collision with car
    for car in car_manager.cars:
        if car.distance(player) < 25:
            scoreboard.game_over()
            game_is_on = False