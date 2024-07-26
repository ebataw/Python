from turtle import Turtle, Screen 
import pandas


doyo = Turtle()
screen =Screen()
score = 0
screen.title("U.S. States game")
image = "states.gif"
screen.addshape(image)
doyo.shape(image)

data = pandas.read_csv("50_states.csv")
states_name = data["state"]
states_list = states_name.to_list()
game_is_on = True

nam = Turtle()


# def get_mouse_click_coor(x, y):
#     print(x, y)

# screen.onscreenclick(get_mouse_click_coor)
# screen.mainloop()
guessd = []

nam.hideturtle()
while len(guessd) < 50:
    answer = screen.textinput(title=f"Guess the state {score}/50", prompt="What's another states's name ?" ).title()
    guessd.append(answer)
    for names in states_list:
        if names == answer:
            print("hiiii")
            score += 1 
            print(score)
            state_ = data[data.state== names]
            state_x = state_.x
            state_y = state_.y
            y_int = state_y.to_list()
            x_int = state_x.to_list()
            nam.hideturtle()
            nam.penup()
            nam.goto(x=x_int[0], y=y_int[0])
            nam.write(arg= f"{names}", align="center", font=("Courier", 7, "normal"))
            print(x_int)
            print(y_int)

screen.mainloop() 