
year=int(input("Enter the year you want to check? "))

if year%4 == 0:
    if year%100==0:
        if  year%400==0:
            print("The year you enterd is a leap year")
        else:
            print("your year is  not a leap year")
    else:
        print("your year is a leap year")
else:
    print("the year you enterd is not a leap year")