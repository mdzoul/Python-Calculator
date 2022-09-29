# Calculator

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

# Operations dictionary
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    
    num1 = float(input("What's the first number? "))
    for symbol in operations:
        print(symbol)
    
    end_calculation = False
    while not end_calculation:    
        operations_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number? "))
        answer = operations[operations_symbol](num1, num2)
        
        print(f"{num1} {operations_symbol} {num2} = {answer}")
    
        to_cont = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        if to_cont == 'y':
            num1 = answer
        else:
            end_calculation = True
            calculator() # This is how you repeat the whole code; This is called recursion

calculator()