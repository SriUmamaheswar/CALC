# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    return x / y

# Dictionary to map operator symbols to functions
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

# Main calculator program
while True:
    print("Select operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Exit")

    choice = input("Enter choice (1-5): ")

    if choice == '5':
        print("Calculator program has ended.")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice in operations:
        result = operations[choice](num1, num2)
        print("Result:", result)
    else:
        print("Invalid input. Please try again.")
