import math

def paint_calc(hight,width,cover):
    can=(hight*width)/cover
    x=math.ceil(can)
    print(f"you will need {x} cans of paint.")

test_h=int(input("hight of the wall: "))
test_w=int(input("width of the wall: "))
coverage=5
paint_calc(hight=test_h, width=test_w, cover=coverage)
