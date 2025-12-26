# Ввод товаров
items = input().split()

# Подсчёт частоты покупок
dict = {}
for item in items:
    if item in dict:
        dict[item] += 1
    else:
        dict[item] = 1

# Частота покупок
print("Purchase frequency:")
for item, count in dict.items():
    print(item + ": " + str(count))

# Самый частый товар
popular = ""
max_count = 0
for item, count in dict.items():
    if count > max_count:
        max_count = count
        popular = item

print("Most popular item:", popular)

# Товары, купленные один раз
print("Purchased once:", end=" ")
for item, count in dict.items():
    if count == 1:
        print(item, end=" ")
print()

# Список пар (частота, товар)
pairs = []
for item, count in dict.items():
    pairs.append((count, item))

# Сортировка по частоте (по убыванию)
pairs.sort(reverse=True)

# Вывод отсортированных товаров
print("Sorted by frequency:")
for count, item in pairs:
    print(item, count)
