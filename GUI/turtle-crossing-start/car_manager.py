import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREAMENT = 10



class CarManager():
    def __init__(self):
        self.cars = []
        self.create_car()
        self.move_increament = 0
        
    def create_car(self):
        for _ in range(0,25):
            random_x = random.randint(-290,290)
            random_y = random.randint(-220,270)
            new_car = Turtle("square")
            new_car.color(f"{random.choice(COLORS)}")
            new_car.penup()
            new_car.shapesize(stretch_len=1.5, stretch_wid=1)
            new_car.goto(random_x, random_y)
            new_car.setheading(180)
            self.cars.append(new_car)
            
    def move_car(self):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE + self.move_increament)
            x_current = car.xcor()
            if int(x_current) < -290:
                random_y = random.randint(-220,270)
                car.goto(290, random_y)
            
    def next_level(self):
        self.move_increament += MOVE_INCREAMENT
        
        
        
        
       
   
        
        
