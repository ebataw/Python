# from turtle import Turtle, Screen 
# timmy=Turtle()
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)
# print(timmy)
# my_screen=Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()
from prettytable import PrettyTable
table=PrettyTable()
table.add_column("name",["pika","ebata"])
table.add_column("type",["pika","eyosiyas"])
table.align="l"
print(table)