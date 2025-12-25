#divisors

n = int(input("number: "))

for i in range(1, n // 2 + 1):
    if n % i == 0:
        print(i, end=" ")

# Add the number itself
print(n)
