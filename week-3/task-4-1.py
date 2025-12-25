# gcd by using Euclid's algorithm

def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

# Input fractions
print("enter: A/B & C/d")
A = int(input("A: "))
B = int(input("B: "))
C = int(input("C: "))
D = int(input("D: "))

# Divide fractions: (A/B) ÷ (C/D) = (A/B) * (D/C) = (A*D)/(B*C)
numerator = A * D
denominator = B * C

# Reduce fraction
common_divisor = gcd(numerator, denominator)
numerator //= common_divisor
denominator //= common_divisor

print("Result:", numerator, "/", denominator)
