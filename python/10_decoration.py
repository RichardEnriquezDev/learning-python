
### Decorators ###
"""
    A decorator is a design pattern in Python that allows a user
    to add new functionality to an existing object without modifying its structure.
    Decorators are usually called before the definition of a function you want to decorate.
"""
# Simple Syntax
def function_decorator(function):
    def function_internal():
        pass # function code
    return function_internal

# Example Simple Syntax
def function_decorator(function):
    def function_internal(*args):
        print("This is an operation.")
        function(*args)
        print("Function success.")
    return function_internal

@function_decorator # Here we decorated a function declared above.
def add_two_numbers(num1, num2):
    return num1 + num2
@function_decorator
def even_or_odd(number):
    return number % 2 == 0
add_two_numbers(10,5) # print() to see
even_or_odd(15)       # print() to see

"""
Other example: This decorator function is a higher order function
that takes a function as a parameter
"""
def uppercase_decoration(function):
    def wrapper():
        var = function()
        uppercase_function = var.upper()
        return uppercase_function
    return wrapper
def speaking():
    print("This is my first speech.")
speaking()
@uppercase_decoration
def speaking():
    return "This is my first speech."
print(speaking())