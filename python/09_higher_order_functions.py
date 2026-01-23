
### Higher Order Functions ###

# A function can take one or more functions as parameters
# A function can be returned as a result of another function
# A function can be modified
# A function can assigned to a variable

### Function as a parameter or argument ###
def speak_up(text):
    return text.upper()
def speak_low(text):
    return text.lower()
# Now create higher order function
def speak_hi(function):
    text = function("Hi Everyone")
    print(text)

speak_hi(speak_up)
speak_hi(speak_low)

### Higher order function that returns a function ###
def divisor(x):
    def divide(y):
        return y / x
    return divide
# return divide function
var_divisor = divisor(2)
print(var_divisor(10))

### Some basic higher order functions ###
# Filter #
""" 
    iterable = []
    filter(function, iterable)
"""
# example
iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filter_pairs = list(filter(lambda x : x%2 == 0, iterable))
print(filter_pairs)
# Map #
""" 
    iterable = []
    map(function, iterables)
"""
# example
cubed = list(map(lambda x : x**3, iterable))
print(cubed)
# Reduce: this returns a single value #
from functools import reduce
""" 
    iterable = []
    reduce(function, iterables)
"""
# example
my_reduce = reduce(lambda x, y : x + y, iterable)
print(my_reduce)