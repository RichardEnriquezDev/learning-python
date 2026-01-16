
### Modules ###
""" A module is a file containing a set of codes or a set of functions """

### Local module ###
# Example
#   from local_dir import my_module 

### Modules import from system and program
""" Uncomment to use """
# # import the module
# import os
# # Creating a directory
# os.mkdir('directory_name')
# # Changing the current directory
# os.chdir('path')
# # Getting current working directory
# os.getcwd()
# # Removing directory
# os.rmdir()

### Math module ###

import math
print(math.pi)           # 3.141592653589793, pi constant
print(math.sqrt(2))      # 1.4142135623730951, square root
print(math.pow(2, 3))    # 8.0, exponential function
print(math.floor(9.81))  # 9, rounding to the lowest
print(math.ceil(9.81))   # 10, rounding to the highest
print(math.log10(100))   # 2, logarithm with 10 as base

### String module ###

import string
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)        # 0123456789
print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

### Random module ###

from random import random, randint
print(random())   # it doesn't take any arguments; it returns a value between 0 and 0.9999
print(randint(5, 20)) # it returns a random integer number between [5, 20] inclusive

### Examples ###
import random 
import string

### function that returns alphanumeric keys ### 
def vita():
    for_range = int(input("Enter a number for the range: "))
    for_argument = int(input("Enter a number for the argument: "))
    for i in range(for_range):
        for_str = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=for_argument))
        print(for_str)        
vita()

### color generating functions ###
### rgb color ###
def generator_color_rgb():
    r = random.randint(0,256)
    g = random.randint(0,256)
    b = random.randint(0,256)
    return r, g, b
    
print(f'rgb{generator_color_rgb()}')

### hex color ###
def rgb_to_hex(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'
rgb_color = generator_color_rgb()
hex_code = rgb_to_hex(rgb_color[0], rgb_color[1], rgb_color[2])
print (hex_code)