from turtle import Turtle
x_stpositions = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20
UP=90
DOWN=270
LEFT=180
RIGHT=0


class Snake:
    def __init__(self,):
        self.turtles = [] 
        self.create_snake()
        self.head = self.turtles[0]

    
    def create_snake(self):
        for position  in x_stpositions:
            self.add_turtles(position)

    def add_turtles(self, position):
            doyo = Turtle(shape="square")
            doyo.penup()
            doyo.color("green")
            doyo.goto(position)
            self.turtles.append(doyo)

    def extend(self):
        self.add_turtles(self.turtles[-1].position())

    def move(self):
        for turt_num in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[turt_num-1].xcor()
            new_y = self.turtles[turt_num-1].ycor()
            self.turtles[turt_num].goto(new_x, new_y)    
        self.head.forward(move_distance)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)   

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head .heading() != RIGHT:
            self.head.setheading(LEFT)
    







































