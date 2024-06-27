
x=["⬜","⬜","⬜"]
y=["⬜","⬜","⬜"]
z=["⬜","⬜","⬜"]

map=[x, y, z]
print("     1     2     3")
print(f"1 {x}\n2 {y}\n3 {z}")
poss=input("Where do you want to put the trasure ")
horizontal=int(poss[0])
vertical=int(poss[1])
selected=map[vertical-1]
selected[horizontal-1]="*"

print(f"{x}\n{y}\n{z}")