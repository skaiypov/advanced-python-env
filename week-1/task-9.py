num = str(input())
arr = list(map(int, num))

if arr[0]+arr[1]+arr[2] == arr[3]+arr[4]+arr[5]:
    print("YES")
else:
    print("NO")
