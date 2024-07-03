from os import system
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)
#Calculator
def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

num1 = int(input("What's the first number?: "))
for symbol in operations:
  print(symbol)

#Here we select "+"
operation_symbol = input("Pick an operation: ") 
num2 = int(input("What's the next number?: "))
calculation_function = operations[operation_symbol]
first_answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {first_answer}")
end_of_code=False
while end_of_code ==False:
    x=input(f"type 'y' to continue calculating with{first_answer} or 'n' if you want to exit: ")
    if x=="y":
        system("cls")
        operation_symbol = input("Pick an operation: ")
        num3 = int(input("What's the next number?: "))
        #Here we select "*" which overides the "+" we selected on line 26.



        #Here the calculation_function selected will be the multiply() function
        calculation_function = operations[operation_symbol] 

        #Here the code will be:
        #second_answer = multiply(multiply(num1, num2), num3)
        second_answer = calculation_function(calculation_function(num1, num2), num3)
        #second_answer = 2 * 3 * 3 = 18
        #To fix this bug we need to change the code on line 42 to:
        second_answer = calculation_function(first_answer, num3)
        #In the next lesson, we will delete all the code from line 34-48 so don't worry
        #It won't affect your final project.
        #But it's a good oportunity to practice debugging. 🐞

        print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")
    else:
        end_of_code=True
