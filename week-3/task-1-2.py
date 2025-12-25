# 3 arrays
def calculate(arr):
    summ = sum(arr)
    mean = summ / len(arr)
    return summ, mean


arr1 = list(map(int, input("first arr: ").split()))
arr2 = list(map(int, input("second arr: ").split()))
arr3 = list(map(int, input("third arr: ").split()))
print()

# First array
s1, m1 = calculate(arr1)
print("Array 1:")
print("Sum:", s1)
print("Mean:", m1)
print()# Input arrays

# Second array
s2, m2 = calculate(arr2)
print("Array 2:")
print("Sum:", s2)
print("Mean:", m2)
print()

# Third array
s3, m3 = calculate(arr3)
print("Array 3:")
print("Sum:", s3)
print("Mean:", m3)
