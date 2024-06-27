
print("Welcome to the love Culculator!" )
name1=input("Enter your name please  \n " )
name2=input("Enter their name please  \n " )

x=name1.lower()
y=name2.lower()

a=x.count("t")
b=x.count("r")
c=x.count("u")
d=x.count("e")

e=x.count("l")
f=x.count("o")
g=x.count("v")
h=x.count("e")

i=y.count("t")
j=y.count("r")
k=y.count("u")
l=y.count("e")

m=y.count("l")
n=y.count("o")
o=y.count("v")
p=y.count("e")

z=a+b+c+d+i+j+k+l
za=e+f+g+h+m+n+o+p

vv=str(z)
ww=str(za)

rr=vv+ww
gg=int(rr) 

if gg <10  or gg > 90:
    print(f"your score is {rr}%, you go like coke and mentos")
elif 40 < gg <50:
    print(f"your score is {rr}%, your alright together")
else:
    print(f"your score is {rr}%")
