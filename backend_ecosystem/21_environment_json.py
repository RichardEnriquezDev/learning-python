""" To build a solid backend ecosystem we need: 
    Environment Management Servers and Containers
    APIs Constructions
    Frameworks Endpoints
    Testing Tools """

# Code Format
""" JSON is a text-based format based on JavaScrip object syntax
    for representing, storing, and exchanging data in web applications.
    It functions in the backend as the standard, lightweight format
    for exchanging, structuring, and transmitting data between the
    server, database, and client."""

# Python to Json
""" Depending on whether you want to obtain a text string or save the
    data to a file, you have two main functions: """

#### We use json.dumps() to convert to a string ###
import json
js = json
# convert list
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot'] 
json_string = js.dumps(vegetables)
print(json_string)
# convert dictionaries
student_dict = {"first_name" : "Richard",
        'last_name':"Enriquez",
        "gender" : "male",
        "age" : 50,
        "marital_status" : "married",
        "skills" : "Python",
        "country" : "Argentina",
        "city" : "Pilar",
        "address" : "Salta 1400",
        }
json_string = js.dumps(student_dict)
json_string = js.dumps(student_dict, indent=4)
# ident=4 it helps to make the result legible ("pretty print").
print(json_string)

#### We use json.dump(), without the s, to save a Json file ###

student_dict = {"first_name" : "Richard",
        'last_name':"Enriquez",
        "gender" : "male",
        "age" : 50,
        "marital_status" : "married",
        "skills" : "Python",
        "country" : "Argentina",
        "city" : "Pilar",
        "address" : "Salta 1400",
        }

with open("example_file.json", "w") as file:
    #json_string = js.dump(student_dict, file)
    json_string = js.dump(student_dict, file, indent=4)

""" Development Environment: To avoid library conflicts, we isolate 
    your project with virtual environments: 
    First, we create a folder with the project name."""

# Inside the folder we create the environment:
""" Create: python -m venv venv
    Activate: source venv/bin/activate """

