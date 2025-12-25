# 2 hipotenuses

import math

# hypotenuse
def hypotenuse(a, b):
    return math.sqrt(a*b + b*b)

# first triangle
a1 = float(input("a = "))
b1 = float(input("b = "))

# second triangle
a2 = float(input("a = "))
b2 = float(input("b = "))

# Calculate hypotenuses
h1 = hypotenuse(a1, b1)
h2 = hypotenuse(a2, b2)

print("Hypotenuse of triangle 1:", h1)
print("Hypotenuse of triangle 2:", h2)

# Compare
if h1 > h2:
    print("first is larger.")
elif h2 > h1:
    print("second is larger.")
else:
    print("they are equal.")
