from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.level = 1
        self.score()


    def score(self):
        self.penup()
        self.goto(-280, 260)
        self.hideturtle()
        self.color("black")
        self.write(arg=f"level:{self.level}", align= "left", font=(FONT) )

    def Game_over(self):
        self.goto(0, 0)
        self.color("black")
        self.write(arg= "Game Over", align="center",  font=("Courier", 24, "normal"))
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.score()
