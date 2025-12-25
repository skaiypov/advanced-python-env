# Euclidean algorithm
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


print("Template: A/B & C/D")

A = int(input("A: "))
B = int(input("B: "))
C = int(input("C: "))
D = int(input("D: "))


numerator = A * D - C * B      # numerator
denominator = B * D           # denominator

# Reduce the fraction
g = gcd(abs(numerator), denominator)
numerator //= g
denominator //= g


print("Result:", numerator, "/", denominator)
