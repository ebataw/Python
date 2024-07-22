from turtle import Turtle, Screen 
from snake import Snake
from food import Food
from scoreboard import Score
import time


# turtle = Turtle()
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)

snake=Snake()
food = Food()
score = Score()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


# detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.count_score()
        snake.extend()
# detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor()  < -300 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_on = False
        score.Game_over()
# detect collision with wall
    for turtles in snake.turtles:
        if turtles == snake.head:
            pass
        elif snake.head.distance(turtles) < 10:
            game_on = False
            score.Game_over()














screen.exitonclick()