#покупки

line = input()

items = line.split()

# словарь
freq = {}

# количество покупок
for item in items:
    if item in freq:
        freq[item] = freq[item] + 1
    else:
        freq[item] = 1

# частота покупок
print("Purchase frequency:")
for item in freq:
    print(item + ":", freq[item])

# самый популярный товар
max_count = 0
popular = ""

for item in freq:
    if freq[item] > max_count:
        max_count = freq[item]
        popular = item

print("Most popular item:", popular)

# товары, купленные один раз
print("Purchased once:", end=" ")
for item in freq:
    if freq[item] == 1:
        print(item, end=" ")
print()

#  сорт
pairs = []

for item in freq:
    pairs.append((freq[item], item))

pairs.sort(reverse=True)

print("Sorted by frequency:")
for count, item in pairs:
    print(item, count)
