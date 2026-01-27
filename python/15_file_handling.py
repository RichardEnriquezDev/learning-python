
### File Handling ###

""" File handling is an import part of programming which
    allows us to create, read, update and delete files. """

# Open(): to handle data in Python

# Syntax
#open('filename', 'mode')
mode_open = open('./intermediate_python/test_data.txt', 'r')

# Modes: 'r', to read the whole text as string
#mode_read = mode_open.read()

#mode_read = mode_open.read(10) #let us print the first 10 character of the text file

# readline(): read only the first line
#mode_read = mode_open.readline()

# readlines(): read all the text line by line and returns a list of line
#mode_read = mode_open.readlines()

# splitlines(): another way to get all the lines as a list
#mode_read = mode_open.read().splitlines()
#print(mode_read)

### Writing and Updating

# 'a' append, we must add a mode as parameter to the open() function
#with open('./intermediate_python/test_data.txt', 'a') as mode_open:
#    mode_open.write('This text has to be append at the end.')

# Create a new file
#with open('./intermediate_python/test_data1.txt', 'w') as mode_open:
#    mode_open.write('This text is a new file.')
mode_open.close()

# Delete files
import os
if os.path.exists('./intermediate_python/test_data1.txt'):
    os.remove('./intermediate_python/test_data1.txt')
    print('Files removed')
else:
    print('The file does not exist')

