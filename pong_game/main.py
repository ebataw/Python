from turtle import Turtle, Screen
from paddle import Paddle 
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width= 800, height= 600)
screen.title("Pong")
screen.tracer(2)

ri_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

screen.listen()
screen.onkeypress(ri_paddle.go_up, "Up")
screen.onkeypress(ri_paddle.go_down, "Down")

screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")
ball = Ball()
score =Scoreboard()


game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # detect collision with roof
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    # detect collision with paddle 
    if ball.distance(ri_paddle) < 50 and ball.xcor() > 320 or  ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    
    # r_paddle missis 
    if ball.xcor() > 390:
        ball.refresh()
        score.l_point()

    
    # l_paddle missis
    if ball.xcor() < -390:
        
        ball.refresh()
        score.r_point()
    
    

screen.exitonclick()
