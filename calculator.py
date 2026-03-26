def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Operation (add/subtract/multiply/divide): ")

if op == "add":
    print(add(num1, num2))
elif op == "subtract":
    print(subtract(num1, num2))
elif op == "multiply":
    print(multiply(num1, num2))
elif op == "divide":
    print(divide(num1, num2))
else:
    print("Invalid operation")