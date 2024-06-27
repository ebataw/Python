print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill=0

if height >= 120:
	print("you can ride the rollercoaster")
	age = int(input("what is your age? "))
	if age < 12:
		bill=5
		print("Child tickets are $5")
	elif age <= 18:
		bill=7
		print("Youth tickets are $7")
	elif age >=45 and age <=55:
		print("your ticket is free ") 
	else:
		print("Adult tickets are $12")
		bill=12
	x=input("do you want a photo taken? please enter Y for yes and N for no ")
	if x =="Y":
		bill=bill+3
	print(f"your final bill is {bill}")
else:
	print("sorry, you have to grow taller before you can ride")



