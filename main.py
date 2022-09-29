# Calculator
import time
from art import logo
from replit import clear
from modules import *

# Operations dictionary
operations = {
    "+": add,
    "-": subtract,
    "x": multiply,
    "/": divide,
    "^": power,
}

def calculator():
    logo()
    num1 = float(input("What's the first number? "))
    symbols = []
    
    end_calculation = False
    for symbol in operations:
            symbols += symbol
        
    while not end_calculation:  
        print(' | '.join(symbols))
        operations_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number? "))
        answer = operations[operations_symbol](num1, num2)

        calculate(num1, operations_symbol, num2, answer)
    
        to_cont = input(f"---\nType 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        if to_cont == 'y':
            num1 = answer
            clear()
            logo()
            print(f"Your previous answer: {answer}")            
        else:
            end_calculation = True
            clear()
            calculator() # This is how you repeat the whole code; This is called recursion

calculator()