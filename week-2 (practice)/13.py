#Показать символы внутри скобок

text = input()

# когда скобки
start = text.find("(")
end = text.find(")")

# вывод
if start != -1 and end != -1 and start < end:
    inside = text[start + 1:end]
    print("Characters inside brackets:", inside)
else:
    print("No valid brackets found")
