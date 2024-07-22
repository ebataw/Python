from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10





class CarManager(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.car_speed = MOVE_INCREMENT
        self.all_car = []

    def creat_car(self):
        self.car_refresh()
    
    def move_car(self):
        for car in self.all_car:
            car.backward(self.car_speed)


    def car_refresh(self):
        self.hideturtle()
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(1, 2) 
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250,250)
            new_car.goto(300, random_y)
            self.all_car.append(new_car)
    def level_up(self):
        self.car_speed += MOVE_INCREMENT


    











