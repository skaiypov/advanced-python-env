# уравнения

s = input() 

a = s[0]
op = s[1]
b = s[2]
# = можно не брать
c = s[4]



# char ---> int
if a != 'x':
    a = int(a)
if b != 'x':
    b = int(b)
c = int(c)

if op == '+':
    if a == 'x':
        x = c - b
    elif b == 'x':
        x = c - a
else:
    if a == 'x':
        x = c + b
    elif b == 'x':
        x = a - c

print(x)