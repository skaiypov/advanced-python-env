# поиск стрел

s = input()
count = 0

for i in range(len(s) - 4):  # -4, чтоб не выйти за границы
    if s[i:i+5] == ">>-->":
        count += 1
    elif s[i:i+5] == "<--<<":
        count += 1

print(count)