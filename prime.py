#Write your code below this line 👇


def prime_checker(number):
    divider=0
    numberx=number
    while number>0:
        if numberx%number==0:
            divider+1
        number-=1
    if divider==2:
        print("this number is prime number")
    else:
        print("the number is not prime number")






#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)