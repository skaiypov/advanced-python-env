# Читаем строки
S1 = input()
S2 = input()

# если длины не равны, сразу NO
if len(S1) != len(S2):
    print("NO")
else:
    # списки из 26 нулей для каждой буквы
    count1 = [0] * 26
    count2 = [0] * 26

    # первый ряд
    for c in S1:
        index = ord(c) - ord('A')  # ascii
        count1[index] += 1

    # второй ряд
    for c in S2:
        index = ord(c) - ord('A')
        count2[index] += 1

    # сравнение
    if count1 == count2:
        print("YES")
    else:
        print("NO")
