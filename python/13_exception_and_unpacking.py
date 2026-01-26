
### Exception Handling ###
""" Python uses try and except to handle errors gracefully.
A graceful exit (or graceful handling) of errors is a simple
programming idiom - a program detects a serious error condition
and "exits gracefully", in a controlled manner as a result.
Graceful handling of errors prevents our applications from crashing."""

""" Syntax
    try:
        program code
    except:
        Execute this code when there is an exception
    else:
        No exceptions? Run this code
    finally:
        Always run this code"""

# Example
try:
    salary = 1800
    #cost = input("Enter your monthly expenses: ") # int in number for TypeError 
    cost = int(input("Enter your monthly expenses: ")) 
    if salary < cost:
        balance = salary - cost
        print("You're in debt. Your balance is: ")
    else:
        balance = salary - cost # Uncomment for NameError
        print("Your accounts are in order. Your balance is: ")
    print('$',balance)
except TypeError:
    print("TypeError occur")
except NameError:
    print("NameError occur")
except ZeroDivisionError:
    print("ZeroDivisionError occur")
else:
    print("Usually run with the try block")
finally:
    print("Always run")

    ### Unpacking ###

""" Allows us to assign a list to variable or multiple variables
    in a single line of code"""

# Example
single_list = [1, 2, 3, 4, 5]
a, b, c, d, e = single_list
print(a,b, c, d, e)

multiply_list = [1, 2, 3, 4, 5]
a, b, c, d, e = multiply_list
print(a)
print(b)
print(c)
print(d)
print(e)

# We can also use two operator: * for tuple and ** for dictionaries
def function_sum(a, b, c, d, e):
    return a + b + c + d + e 
#print(function_sum(single_list)) # this will cause an error
print(function_sum(*single_list)) # this mode we have access to all the arguments 

numbers = range(2, 7)  # normal call with separate arguments
print(list(numbers)) # [2, 3, 4, 5, 6]
args = [2, 7]
numbers = range(*args)  # call with arguments unpacked from a list
print(numbers)      # [2, 3, 4, 5,6]

# Unpacking dictionaries
# as argument for a function
def person_date(name, country, city, age):
    print(f'My name is {name}, and live in {country},in the city {city}, and {age} years old')
dct = {'name':'Richard', 'country':'Argentina', 'city':'Pilar', 'age':50}
person_date(**dct)
print(*dct) # this mode accessing to dictionaries keys

# *args: we can define functions with a variable numbers arguments
def add_numbers(*args):
    return sum(args)
print(add_numbers(5, 6)) 

# **kwargs
# They allow us to give a name to each input argument,
# and to access them within the function through a dictionary.
def add_numbers(**kwargs):
    s = 0
    for key, value in kwargs.items():
        print(key, "=", value)
        s += value
    return s
    
print(add_numbers(a=3, b=10, c=3))