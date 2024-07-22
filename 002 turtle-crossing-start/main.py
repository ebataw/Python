import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car = CarManager()
score = Scoreboard()
screen.listen()
screen.onkey(player.go_up, "Up")



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.creat_car()
    car.move_car()

    
    for cars in car.all_car:
        if cars.distance(player) < 20:
            score.Game_over()
            game_is_on = False

    if player.is_at_finish():
        player.refresh()
        car.level_up()
        score.level +=1
        score.update_score()




screen.exitonclick()
