
### Some basic types error ###
"""
Uncomment to see the error
"""
# SyntaxError
# print "hello everyone"  #SyntaxError: Missing parentheses
print("hello everyone")

# NameError
#print(age)  #NameError: name 'age' is not defined
age = 50
print(age)

# IndexError
numbers = [1, 2, 3, 4, 5]
#numbers[5]  #IndexError: list index out of range
numbers[4]

# ModuleNotFoundError
#import maths  #ModuleNotFoundError: No module named 'maths'
import math

# AttributeError
import math
#math.PI  #AttributeError: module 'math' has no attribute 'PI'
math.pi

# KeyError
users = {'name':'Richard', 'age':50, 'country':'Argentina'}
users['name']
#users['county']  #KeyError: 'county'
users['country']

# TypeError
#4 + '3'  #TypeError: unsupported operand type(s) for +: 'int' and 'str'
4 + int('3')
4 + float('3')

# ImportError
#from math import power  #ImportError: cannot import name 'power'
from math import pow

# ValueError
#int('12b') #ValueError: invalid literal for int() with base 10: '12b'
int('12')

# ZeroDivisionError
#1 / 0 #ZeroDivisionError: division by zero