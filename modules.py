import time
from replit import clear
from art import logo

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

# Power
def power(n1, n2):
    return n1 ** n2

# Calculating
def calculate(num1, operations_symbol, num2, answer):
    clear()
    logo()
    print("Calculating.")
    time.sleep(0.5)
    print("Calculating..")
    time.sleep(0.5)
    print("Calculating...")
    time.sleep(0.5)
    clear()
    logo()
    print(f"{num1} {operations_symbol} {num2} = {answer}")