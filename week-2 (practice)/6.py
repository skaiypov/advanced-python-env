#Удалить все "a" и посчитать удалённые

text = input()

new_text = ""
count_removed = 0

for char in text:
    if char.lower() == "a": 
        count_removed += 1
    else:
        new_text += char

print("New string:", new_text)
print("Letters removed:", count_removed)
