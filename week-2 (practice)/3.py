#Удалить точки и посчитать, сколько убрали

text = input()

new_text = ""
count = 0

for char in text:
    if char == ".":
        count += 1
    else:
        new_text += char

print("New string:", new_text)
print("Dots removed:", count)
