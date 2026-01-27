
### PIP PYTHON PACKAGE MANAGER ###

""" PIP stands for Preferred installer program. We use pip to install
different Python packages. Package is a Python module that can contain
one or more modules or other packages. A module or modules that we can
install to our application is a package. """

# Installing packages using pip 
# numpy: is one of the most popular packages in machine learning and data science community.
""" in console: pip install numpy """
import numpy
numpy.version.version # print() to see

vegetables = [1, 2, 3, 4, 5]
np_array = numpy.array(vegetables)
len(np_array)
print(np_array * 2)

""" Pandas: is an open source, BSD-licensed library providing
high-performance, easy-to-use data structures and data analysis tools
for the Python programming language. """

""" Webbrowser: a web browser module, which can help us to open any
    website. """
import webbrowser

# list url:
url_list = [
    'https://github.com/RichardEnriquezDev',
    'http://www.python.org'
]
for urls in url_list:
    webbrowser.open_new_tab(urls)

""" Further information about package: request, SQL, Django, Flask
    PyQuery and more; you can see them in others courses. """