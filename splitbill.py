import random
name_string=input("Give me evrybody's names, Seprated by a Comma. ")
name=name_string.split(",")
# print(name)

x=len(name)
y=random.randint(0,x-1)
# print(y)

z=name[y]
print(f"The payer is " +z)