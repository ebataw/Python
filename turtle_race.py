from turtle import Turtle,Screen
import random

doyo = Turtle()
# oli = Turtle()
# eba = Turtle()
# muna = Turtle()
# hani = Turtle()
# busu = Turtle()

colors = ["red", "orange", "green", "purple", "yellow", "blue"]
y_pos = [-70, -40, -10, 20, 50, 80]
all_turtle = []





scree = Screen()
scree.setup(500, 400)



doyo.hideturtle()
x_input=scree.textinput("User List", "how many players are there")
x_inputs = int(x_input)

users_list={}

info=0
so=0
infos=[]
if x_inputs < 6:
    if x_inputs==1:
        for turtle_index  in range (0, 6):
            new_turtle = Turtle(shape="turtle")
            new_turtle.penup()
            new_turtle.color(colors[turtle_index])
            new_turtle.goto(x=-250, y= y_pos[turtle_index])
            all_turtle.append(new_turtle)
        info += 1
        user_data = scree.textinput("user data", f"please enter your name player{info}")
        user_bet=scree.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")
        infos.append(user_data)
        names= {
            user_data:user_bet
                }
        users_list.update(names)
    else:
        for turtle_index  in range (0, x_inputs):
                new_turtle = Turtle(shape="turtle")
                new_turtle.penup()
                new_turtle.color(colors[turtle_index])
                new_turtle.goto(x=-250, y= y_pos[turtle_index])
                all_turtle.append(new_turtle)
        for  users in range(x_inputs):
            info += 1
            user_data = scree.textinput("user data", f"please enter your name player{info}")
            user_bet=scree.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")
            infos.append(user_data)
            names= {
                user_data:user_bet
                    }
            users_list.update(names)
else:
    is_race_on = False 
    print(" input above user limit ")





if user_bet:
    is_race_on = True
else:
    print("invalid input, please try again ")

while is_race_on:

    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning=turtle.pencolor()
            if x_inputs==1:
                ko=infos[so]
                if winning == user_bet:
                    # print(f"you won the game {ko}")
                    pass
                else:
                    # print(f"you have lost the game {ko}")
                    pass
            else:
                for i in infos:
                    row=users_list[i]
                    kor=infos[so]
                    if winning == row:
                        # print(f"{row} won the game")
                        pass
                    else:
                        # print(f"you have lost the game {row}")
                        pass

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)









scree.exitonclick()