from turtle import *
import random
speed(0)
# doyo=Turtle()
# def draw_shape(num_side):
#     angle=360/num_side
    # for _ in range(num_side):
    #     color=("red","blue","green") 
    #     for c in color:
#             doyo.speed(10)
#             doyo.pensize(10)
#             doyo.forward(100)
#             doyo.color(c)
#             doyo.right(angle)

# for shape_side_n in range(3, 11):
# t=Turtle()
colormode(255)


# for i in range(100):
#         color=("red","blue","green") 
#         for c in color:
#             steps = 10
#             angle = 90
            # t.color(c)
            # t.pensize(10)
            # t.speed(10)
#             t.right(angle)
#             t.fd(steps)
#             # t.bk(steps)
#             t.rt(10)
#             t.lt(10)



directions=[0, 90, 180, 270]
# for i in range(100):
#     # x=random.choice(directions)
#     # x=set[z]
#     color=("red","blue","green")
#     for c in color:
#         steps = 30 
#         angle = 90
#         t.color(c)
#         t.pensize(10)
#         t.speed(10)
#         t.right(random.choice(directions))
#         t.forward(steps)
        # t.left(random.choice(directions))
# colores=["red","blue","green"]


def rondom():
    r=random.randint(0, 255)
    g=random.randint(0, 255)
    b=random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

# for i in range(200):
#     pensize(15)
#     speed(0)
#     color(rondom())
#     fd(30)
#     setheading(random.choice(directions))


for _ in range(100):
    color(rondom())
    circle(100)
    curent=heading()
    setheading(curent + 10)









scree=Screen()
scree.exitonclick() 