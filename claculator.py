equation = input("Equation: ")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

equation = [item for item in equation.split()]
#equation = ["5", "/", "2"]

if equation[1] == "+":
    print(int(equation[0]) + int(equation[2]))
elif equation[1] == "-":
    print(int(equation[0]) - int(equation[2]))
elif equation[1] == "*":
    print(int(equation[0]) * int(equation[2]))
elif equation[1] == "/":
    print(int(equation[0]) / int(equation[2]))
elif equation[1] == "**":
    print(int(equation[0]) ** int(equation[2]))