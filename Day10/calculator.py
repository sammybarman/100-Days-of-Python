from art import logo 

def calculate(a,b):
    return a+b,a-b,a*b,a/b

def calculator(a,b):
    print(logo)
    print("Select the operation you want to perform: ")
    print("+")
    print("-")
    print("*")
    print("/")
    operation = input("Enter the operation: ")

    if operation == "+":
        print(f"{a} + {b} = {calculate(a,b)[0]}")
        return a+b
    elif operation == "-":
        print(f"{a} - {b} = {calculate(a,b)[1]}")
        return a-b
    elif operation == "*":
        print(f"{a} * {b} = {calculate(a,b)[2]}")
        return a*b
    elif operation == "/":
        print(f"{a} / {b} = {calculate(a,b)[3]}")
        return a/b
    else:
        print("Invalid operation")
        return
    
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
x = calculator(a,b)
while True:
    again = input("Do you want to continue with the same numbers? (y/n): ")
    if again == "y":
        a = x
        b = float(input("Enter the second number: "))
        x = calculator(a,b)
    elif again == "n":
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        calculator(a,b)
    else:
        print("Invalid input")
        break

