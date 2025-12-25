# area of the 3 rectangles

def area():
    length = float(input("a = "))
    width = float(input("b ="))
    area = length * width
    print("Area:", area)
    print()

for i in range(3):
    print("Rectangle", i+1)
    area()
    i+=1

