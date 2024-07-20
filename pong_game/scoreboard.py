from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    
    def update_score(self):
        self.goto(-50, 200)
        self.write(self.l_score, "center", font=("Courier", 50, "normal"))
        self.goto(50, 200)
        self.write(self.r_score, "center", font=("Courier", 50, "normal"))

    def l_point(self):
        self.l_score += 1
        self.clear()
        self.update_score()


    def r_point(self):
        self.r_score += 1
        self.clear()
        self.update_score()
