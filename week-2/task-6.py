#дополнение

lst = ["hi", "hello", "hey"]

# макс длина
max_len = 0
for s in lst:
    if len(s) > max_len:
        max_len = len(s)

# новый список
result = []

for s in lst:
    need = max_len - len(s)
    result.append(s + "_" * need)

print(result)
