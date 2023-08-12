# Python 3.x

print("Please enter the first number:")
num1 = int(input())

print("Please enter the second number:")
num2 = int(input())

print("Please enter the operation (+, -, *, /):")
op = input()

result = None

if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Error: Invalid operation")

if result is not None:
    print("The result is:", result)
