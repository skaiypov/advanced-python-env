#Заменить ":" на "%" и посчитать замены 


text = "10:30:45"

new_text = ""
count = 0

for char in text:
    if char == ":":
        new_text += "%"
        count += 1
    else:
        new_text += char

print("new text:", new_text)
print("reps number:", count)
