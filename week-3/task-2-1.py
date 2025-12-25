# area of hex by triangles

import math


# input side of hexagon
a = float(input("side: "))

# height(triangle)
h = (math.sqrt(3)/2) * a

# S(hex) = 6 * S(triangle)
hex_area = 6 * (0.5 * (a*h))
print("Area:", hex_area)
