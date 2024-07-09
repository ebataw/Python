import random 
from os import system
logo="""
                                  _    _                                      _                                                             
   __ _  _   _   ___  ___  ___   | |_ | |__    ___    _ __   _   _  _ __ ___  | |__    ___  _ __  
  / _` || | | | / _ \/ __|/ __|  | __|| '_ \  / _ \  | '_ \ | | | || '_ ` _ \ | '_ \  / _ \| '__| 
 | (_| || |_| ||  __/\__ \\__ \  | |_ | | | ||  __/  | | | || |_| || | | | | || |_) ||  __/| |    
  \__, | \__,_| \___||___/|___/   \__||_| |_| \___|  |_| |_| \__,_||_| |_| |_||_.__/  \___||_|    
   __/ |                                                                                        
  |___/                                                                                                                                                                                                                                             
"""
print(logo)
print("Wellcome to guess the number.")
print("I'm thinking of a number between 1 and 100")
x=input("Choose a difficultiy: 'Easy' or 'Hard': ").lower()
difficultiy=0

if x=="easy":
    difficultiy+=2
elif x=="hard":
    difficultiy+=3

random_number=random.randint(0,100)
if difficultiy==2:
    turns=10
    system("cls")
    while turns>0:
        print(f"You have {turns} attempts remaining to guess the number")
        y=input("Make a guess\n")
        turns-=1
        n=int(y)
        if n>random_number:
            print("Your number is higher")
        if n<random_number:
            print("Your number is lower")
        if n==random_number:
            print("You won")
            turns=0
    if turns==0:
        print("GAME OVER")

if difficultiy==3:
    turns=5
    system("cls")
    while turns>0:
        print(f"You have {turns} attempts remaining to guess the number")
        y=input("Make a guess\n")
        turns-=1
        n=int(y)
        if n>random_number:
            system("cls")
            print("Your number is higher")
        if n<random_number:
            system("cls")
            print("Your number is lower")
        if n==random_number:
            system("cls")
            print("YOU WON")
            turns=0
    if turns==0:
        print(f"The number was {random_number}")
        print("GAME OVER")


