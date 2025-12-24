#Посчитать все буквы "t"

text = input("Enter a line: ")

count = 0

for char in text:
    if char.lower() == "t":  
        count += 1

print("Number of 't's in the string:", count)
