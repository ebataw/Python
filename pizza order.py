
print("welcome to python pizza Deliveries")
size=input("what size pizza do you want?S, M or L ") 
pep=input("Do you want pepperoni? Y or N ")
che=input("Do you want extra cheese? Y or N ")

cost=0

if size=="S":
    cost +=15
elif size =="M":
    cost +=20 
elif size =="L":
    cost +=25


if pep =="Y":
    cost +=2
if che == "Y":
    cost +=1
print(f"Your bill is ${cost}")
