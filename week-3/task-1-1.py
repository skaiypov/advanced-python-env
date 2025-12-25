# calculate areas of shapes


import math
print("Choose a shape:")
print("1. Square")
print("2. Rectangle")
print("3. Circle")
print()
choice = input()

if choice == "1":
    a = float(input("a = "))
    area = a * a
    print("Area of the square:", area)
elif choice == "2":
    a = float(input("a ="))
    b = float(input("b ="))
    area = a * b
    print("Area of the rectangle:", area)
elif choice == "3":
    r = float(input("R ="))
    area = math.pi * r * r
    print("Area of the circle:", area)

