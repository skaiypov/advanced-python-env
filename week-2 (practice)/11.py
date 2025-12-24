#Найти самую длинную последовательность "n" и заменить "!" на "."

text = input()

max_n = 0
current_n = 0

for char in text:
    if char.lower() == "n":  
        current_n += 1
        if current_n > max_n:
            max_n = current_n
    else:
        current_n = 0

# змена
new_text = text.replace("!", ".")

print("Longest sequence of 'n':", max_n)
print("Converted string:", new_text)
