import turtle as t
import random


doyo = t.Turtle()
t.colormode(255)
doyo.speed(0)
def rondom():
    r=random.randint(0, 255)
    g=random.randint(0, 255)
    b=random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


def  draw_P(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        doyo.color(rondom())
        doyo.circle(100)
        curent=doyo.heading()
        doyo.setheading(curent + size_of_gap)
        doyo.hideturtle


draw_P(5)





s=t.Screen()
s.exitonclick