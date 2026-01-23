
### List Comprehension ###

""" List comprehension in Python is a compact way of creating a list from a sequence.
It is a short way to create a new list.
List comprehension is considerably faster than processing a list using the for loop."""

# syntax
# [expression for i in iterable if condition]

# Examples: change a string to a list of characters #
str_to = "Python"
to_list = [i for i in str_to]
print(to_list)

# Generate a list number and mathematical operations #
number_to_list = [i for i in range(11)]
print(number_to_list)
operation_number = [i * i for i in range(11)]
print(operation_number)

# Filter #
numbers_pan = [i for i in range(-5, 15)]
print(numbers_pan)
filter_numbers_pan = [i for i in numbers_pan if i > 0]
print(filter_numbers_pan)

# lists of lists to a one dimensional list #
list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [i for row in list_of_lists for i in row]
print(flattened_list)

# create a list of tuple #
list_of_tuple = [(i, 1 * 1, i * 1, i * i, i * i * i, i * i * i * i, i * i * i * i * i) for i in range(11)] 
print(list_of_tuple)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened_countries = [i for row in countries for i in row]
print(flattened_countries)