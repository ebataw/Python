from turtle import Turtle

class Score(Turtle):
    def __init__(self) :
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.update_score()
        with open("data.txt",mode="w") as fe:
            fe.write(str(self.high_score))


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt",mode="w") as fe:
                fe.write(f"{self.high_score}")
        self.score = 0
        self.update_score()



    def update_score(self):
        with open("data.txt", mode= "r") as fe:
            self.clear()
            self.write(arg= f"Score:{self.score}  High score: {fe.read()}", align="center",  font=("Courier", 14, "normal"))



    def count_score(self):
        self.score += 1
        self.clear()
        self.update_score()


