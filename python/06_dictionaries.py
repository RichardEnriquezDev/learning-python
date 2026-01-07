
""" A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type. """

""" Creating a Dictionary """
# Syntax
emty_dict = {} # To create a dictionary we use curly brackets, {} or the dict() built-in function.
dict()

# example
dog = {}

""" Adding Items to a Dictionary """
dog["name"] = () # A dictionary must have a key and a value
dog["color"] = () # color is the key, value is none, but can be added black, dog = {"color : black"}
dog["breed"] = ()
dog["legs"] = ()
dog["age"] = ()

student_dict = {"first_name" : "Richard",
        'last_name':"Enriquez",
        "gender" : "male",
        "age" : 50,
        "marital_status" : "married",
        "skils" : "Python",
        "country" : "Argentina",
        "city" : "Pilar",
        "address" : "Salta 1400",
        }

""" It checks the number of 'key: value' pairs in the dictionary """
len(student_dict)

""" We can access Dictionary items by referring to its key name."""
student_dict["skils"] 
type(student_dict["skils"]) # accesing to type of value

""" We can modify items in a dictionary """
student_dict["skils"] = "Javascript, Python"

""" Getting Dictionary Keys as a List """
student_dict.keys() # method gives us all the keys of a a dictionary as a list
student_dict.values() # method gives us all the values of a a dictionary as a list

""" Changing Dictionary to a List of Items """
student_dict.items()

""" Removing Key and Value Pairs from a Dictionary """
student_dict.pop("address")# pop(key): removes the item with the specified key name:
student_dict.popitem() # popitem(): removes the last item
del emty_dict # del: removes an item with specified key name
print(student_dict)