# Find all natural numbers not exceeding the given n that are divisible by each of their digits

n = int(input("number: "))

# Loop through all numbers from 1 to n
for i in range(1, n + 1):
    s = str(i)  # convert number to string to check digits
    divisible = True
    
    for digit in s:
        d = int(digit)
        if d == 0 or i % d != 0:
            divisible = False
            break
    
    if divisible:
        print(i, end=" ")
