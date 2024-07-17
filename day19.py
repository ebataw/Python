from turtle import Turtle, Screen 

doyo = Turtle()
scree = Screen()
doyo.speed(0)

def move_fd():
    doyo.forward(10)

def move_bk():
    doyo.backward(10)


def move_cls():
    doyo.reset()


def move_cl():
    new=doyo.heading() +10
    doyo.setheading(new)

def move_ccl():
    new=doyo.heading() -10
    doyo.setheading(new)

scree.listen()
scree.onkey(key="w", fun=move_fd)
scree.onkey(key="s", fun=move_bk)

scree.onkey(key="c", fun=move_cls)
scree.onkey(key="d", fun=move_cl)
scree.onkey(key="a", fun=move_ccl)


















scree.exitonclick()