# Swap the first and last elements

def swap(arr):
    if len(arr) > 1:
        arr[0], arr[-1] = arr[-1], arr[0] 

# Input length of the array
leng = int(input("length: "))

# Input
arr = []
for i in range(leng):
    x = int(input())
    arr.append(x)

print("original:", arr)
swap(arr)

# Output resulting array
print("after swapping:", arr)


