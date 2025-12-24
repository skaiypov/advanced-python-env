#В первой половине строки заменить "n" на "*"

text = input()
n = len(text)
half = n // 2 

new_text = ""

for i in range(n):
    if i < half and text[i].lower() == "n":
        new_text += "*"
    else:
        new_text += text[i]

print("Original string:", text)
print("Converted string:", new_text)
