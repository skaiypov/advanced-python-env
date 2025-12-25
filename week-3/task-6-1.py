#GCD, LCM

def gcd_count(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Input two natural numbers
A = int(input("A: "))
B = int(input("B: "))

# Calculate GCD
gcd = gcd_count(A, B)

# LCM formula: LCM(A, B) = (A * B) / GCD(A, B)
print("GCD:", gcd)
print("LCM:", (A * B) // gcd)
