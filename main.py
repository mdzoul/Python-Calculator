# Calculator
import time
from art import logo
from replit import clear

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

# Calculating
def calculate():
    clear()
    logo()
    print("Calculating.")
    time.sleep(0.5)
    print("Calculating..")
    time.sleep(0.5)
    print("Calculating...")
    time.sleep(0.5)
    clear()

# Operations dictionary
operations = {
    "+": add,
    "-": subtract,
    "x": multiply,
    "/": divide,
}

def calculator():
    logo()
    num1 = float(input("What's the first number? "))
    symbols = []
    for symbol in operations:
        symbols += symbol
    print(' | '.join(symbols))
    
    end_calculation = False
    while not end_calculation:    
        operations_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number? "))
        answer = operations[operations_symbol](num1, num2)

        calculate()

        logo()
        print(f"{num1} {operations_symbol} {num2} = {answer}")
    
        to_cont = input(f"---\nType 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        if to_cont == 'y':
            num1 = answer
        else:
            end_calculation = True
            calculator() # This is how you repeat the whole code; This is called recursion

calculator()