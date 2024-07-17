###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
from turtle import Turtle,Screen
# import colorgram
import random
# rgb_colors = []
# colors = colorgram.extract('images.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
doyo = Turtle()
scree = Screen()

scree.colormode(255)
doyo.speed(0)

# print(rgb_colors) 
color_list = [ (140, 165, 191), (21, 33, 52), (212, 157, 114), (198, 140, 149), (62, 104, 134), (141, 177, 162), (148, 72, 62), (232, 211, 107), (142, 27, 34), (48, 30, 35), (139, 68, 76), (26, 51, 44), (65, 109, 95), (53, 30, 25), (228, 168, 174), (188, 96, 105), (131, 32, 27), (230, 172, 164), (199, 93, 79), (19, 92, 69), (174, 188, 216), (38, 60, 99), (112, 123, 156), (170, 204, 194), (53, 150, 184), (161, 203, 216)]  
# doyo.pos()
# print(doyo.pos())


doyo.pencolor("white")

doyo.setheading(225)
doyo.fd(300)
doyo.setheading(0)
doyo.color("white")
num_of_dots = 100
doyo.hideturtle()

# doyo.home()
# doyo.left(50)
# doyo.forward(100)
# doyo.pos()

# print(round(doyo.xcor(), 5))


# doyo.home()
# doyo.left(60)
# doyo.forward(100)
# print(doyo.pos())
# doyo.pencolor("white")
# print(round(doyo.ycor(), 5))

def rondom():
    r=random.randint(0, 255)
    g=random.randint(0, 255)
    b=random.randint(0, 255)
    random_color = (r, g, b)
    return random_color
def new_random():
    x=random.choice(color_list)
    return x


for dot_count in range(1, num_of_dots+1):
    new_random()


    # doyo.penup()
    doyo.dot(20, random.choice(color_list) )
    doyo.penup()
    doyo.fd(50)


    if dot_count % 10 == 0:
        doyo.setheading(90)
        doyo.fd(50)
        doyo.setheading(180)
        doyo.fd(500)
        doyo.setheading(0)




scree.exitonclick()