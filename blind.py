from os import system

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
''' 
print(logo)
key=input("Welcome to the secret auction program.What is your name?:")
value=input("What's your bid?:")
bid = {}
bid [key]=value

end_of_bid=False
while end_of_bid==False:
    option=input("Are there any other bidders? Type 'yes' or 'no'.")
    if option=="yes":
        system("cls")
        key=input("Welcome to the secret auction program.What is your name?:")
        value=input("What's your bid?:")
        bid [key]=value
    if option=="no":
        end_of_bid=True

# print(bid)
max_key=""
max_val=0
x=str(max_val)
for key,value in bid.items():
    if value>x:
        max_val=value
        max_key=key
print(f"the winer is {max_key}, with ${max_val} bid  ")