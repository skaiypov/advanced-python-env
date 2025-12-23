# разрешённые буквы


letters = "ABCEHKMOPTXY"

n = int(input())

for _ in range(n):
    s = input()

    ok = True

    # проверка длины
    if len(s) != 6:
        ok = False

    else:
        # позиции
        if s[0] not in letters:
            ok = False

        if not s[1].isdigit() or not s[2].isdigit() or not s[3].isdigit():
            ok = False

        if s[4] not in letters or s[5] not in letters:
            ok = False

    if ok:
        print("Yes")
    else:
        print("No")
