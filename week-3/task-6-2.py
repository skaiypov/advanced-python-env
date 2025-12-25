# area of a convex quadrilateral 

import math

# Heron's formula
def triangle_area(a, b, c):
    p = (a + b + c) / 2 
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

# sides
AB = 3
BC = 4
CD = 5
AD = 6
AC = 5  # diagonal

# Area of two triangles
area1 = triangle_area(AB, BC, AC) 
area2 = triangle_area(AD, CD, AC) 

print("quadrilateral area:", area1 + area2)
