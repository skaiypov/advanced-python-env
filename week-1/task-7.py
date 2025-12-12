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
    print("Result: ", int(a/b) if b != 0 else "Division by zero is forbidden!")


