print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
x=input("where would you like to go ,left or right \n ")

if x=="left":
    y=input("Congrats! you have servived the first challenge, do you want to wait for a boat or swim over to the island \n ")
    if y =="wait":
        z=input("You have succesfully landed on the island there are three doors Yellow, Red and Blue which door do you want to go through \n ")
        if z=="Red":
            print("You have been burned by fire,GAME OVER!!!")
        elif z=="Yellow":
            print("Congrats!!,you have succesfully collected your treasure")
        elif z=="blue:":
            print("You have been eaten by beasts,GAME OVER!!!")
        else:
            print(" invalid input,GAME OVER !!!!")
    else:
        print("You have been eaten by a dolphin,GAME OVER!!!")
else:
    print("You have fallen in to a hole,GAME OVER!!GAME OVER!!!")