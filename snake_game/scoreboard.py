from turtle import Turtle

class Score(Turtle):
    def __init__(self) :
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.update_score()


    def Game_over(self):
        self.goto(0, 0)
        self.color("white")
        self.write(arg= "Game Over", align="center",  font=("Courier", 24, "normal"))
        self.hideturtle()



    def update_score(self):
        self.write(arg= f"Score: {self.score}", align="center",  font=("Courier", 14, "normal"))



    def count_score(self):
        self.score += 1
        self.clear()
        self.update_score()


