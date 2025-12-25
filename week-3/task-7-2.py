# octal code

n = int(input("non-negative num: "))

oct = format(n, "o") #octal

# how many zeros to add
zeros = 10 - len(oct)

# Add leading zeros
output = "0" * zeros + oct

print("10-digit octal code:", output)
