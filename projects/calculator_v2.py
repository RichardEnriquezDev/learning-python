
######## Personal Calculator ##########



def ask_for_number():
    while True:
        try:
            a = float(input("Enter firt number: "))
            b = float(input("Enter second number: "))
            return a, b
        except ValueError:
            print("Put only number, please: ")
            
def add (a, b):
    return a + b
def subtract (a, b):
    return a - b
def multiply (a, b):
    return a * b
def divide (a, b):
    return a / b
def power (a, b):
    return a ** b
def percentage (a, b):
    return a * b / 100

operations ={
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
    "**": power,
    "%" : percentage
}

operation_symbols = list(operations.keys())

def show_menu(title, options, extra_option=None):
    print("\n" + title)
    for i, option in enumerate(options, start=1):
        print(f"{i}) {option}")
    
    if extra_option:
        print(f"{len(options) + 1}) {extra_option}")


while True:
    show_menu(
        "CALCULATOR - OPERATIONS\n",
        operation_symbols,
        "Exit"
    )
    
    choice = input("\nEnter an option: ")
    
    if not choice.isdigit():
        print("\nEnter a number.")
        continue
    choice = int(choice)

    
    if choice == len(operation_symbols) + 1:
        print("Close calculator.")
        break
    
    if  1 <= choice <= len(operation_symbols):
        operador = operation_symbols[choice - 1]
        num_1 , num_2 = ask_for_number()
    
        try:
            resultado = operations[operador](num_1, num_2)
            print("\nThe result is:", resultado)
        except ZeroDivisionError:
            print("Error: cannot divide by zero.")

    else:
        print("\nOption invalid.")