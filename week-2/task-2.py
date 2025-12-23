#циклические сдвиги 

a = input()
b = input()

count = 0
m = len(b)
bb = b + b

for i in range(len(a) - m + 1):
    sub = a[i:i + m]
    if sub in bb:
        count += 1

print(count)