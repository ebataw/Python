stu_hight=input("input a list of students heights ").split()
for n in range(0, len(stu_hight)):
    stu_hight[n]=int(stu_hight[n])
# print(stu_hight)

s=0
z=0
for x in stu_hight:
    s+=x
    z+=1

# print(s)
# print(z)
y=s/z
# print(y)

f=round(y)
print(f)