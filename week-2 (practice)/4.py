#Заменить "a" на "o", посчитать замену и длину строки

text = input()

new_text = ""
count_replacements = 0

for char in text:
    if char.lower() == "a":
        new_text += "o"
        count_replacements += 1
    else:
        new_text += char

total_characters = len(new_text)

print("New string:", new_text)
print("Replacements made:", count_replacements)
print("Total characters:", total_characters)
