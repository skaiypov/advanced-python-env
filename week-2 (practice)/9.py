#Посчитать, сколько раз встречается заданное слово

text = "This is a test. test test"
find = "test"

words = text.lower().split()
find = find.lower()

count = 0
for w in words:
    # убрать знаки припинания
    w = w.strip(".,!?")
    if w == find:
        count += 1

print(f"The word '{find}' occurs {count} times.")
