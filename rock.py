rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
user=(input("What do you choose? Type 0 for Rock,1 for paper or 2 for scissors "))
# rock=0
# paper=1
# scissors=2
x=random.randint(0,2)
a=int(user)
z=[rock,paper,scissors]
y=z[a]
print("yours:")

print(y)
r=z[x]
print("computer:")

print(r)
if a==x:
    print("the game is a draw")
if a==1  and x==0:
        print("you won the game")
if a==1 and x==2: 
    print("computer won the game")
if a==0 and x==1:
    print(" computer won the game ")
if a==0 and x==2: 
    print("you won the game")
if a==2 and x==0:
    print("computer won the game")
if a==2 and x==1:
    print("you won the game")




# if a==1  and x==0:
#         print("you won the game")
# elif x==1:
#     print("the game is a draw ")
# elif x==2: 
#     print("computer won the game")
# else:
#     print("v")

# if a==2 and x==0:
#     print("computer won the game")
# elif x==1:
#     print("you won the game ")
# elif x==2: 
#     print("the game is a draw")
# else:
#     print("v")
# rock=0
# paper=10
# scissors=2