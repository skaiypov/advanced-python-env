#уникальные слова

n, m = map(int, input().split())
text = input()

words = []
count = 0  # количество уникальных слов

for i in range(n - m + 1):
    sub = text[i:i + m]
    # встречалась ли раньше
    already = False
    for j in range(count):
        if words[j] == sub:
            already = True
            break
    if not already:
        words += [sub]  # + в список
        count += 1

print(count)