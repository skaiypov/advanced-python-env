a = int(input("First number: "))
x = input("Operation (+, -, *, /): ")
b = int(input("Second number: "))

print()
if x == '+':
    print("Result: ", a+b)
elif x == '-':
    print("Result: ", a-b)
elif x == '*':
    print("Result: ", a*b)
elif x == '/':
    print("Result: ", a/b)