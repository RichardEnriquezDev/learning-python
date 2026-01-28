""" This part corresponds to the programming paradigm known as
    object oriented programming. """

### Class: we create class to create a object ###

# A person, a dog and a car, can be represented by a class
# Example
""" A Class it is a template that defines characteristics and behavior
    of an object. """
class Person: # create a class person
    pass
class Dog: 
    pass
class Car: 
    pass

""" Class constructor: Python has a built-in init() constructor function.
    The init constructor function has self parameter which is a reference to the current instance of the class.
"""    
class Person:
    species = "Homo sapiens"  # this is a class attribute

    def __init__(self, lastname, age, country ): # This is a constructor

        self.lastname = lastname # these are instance attributes
        self.age = age
        self.country = country
""" Instance: a specific object created from the template called Class. """
one_person = Person('Enriquez', 50, 'Pilar')
print(one_person.lastname)
print(one_person)

""" Methods: the behaviors of an object. """
class Person:
    species = "Homo sapiens"
    def __init__(self, lastname, age, country ):
        self.lastname = lastname
        self.age = age
        self.country = country
    # The methods are functions which belong to the object
    def person_skill(self, skills):
        self.skill = []
        self.skill.append(skills)
    def introduce(self):
        if self.age > 18:
            print(f'Hi my name is {self.lastname} and I am {self.skill}')
        else:
            print(f'Hi my name is {self.lastname} and I am a student.')

one_person = Person('Enriquez', 50, 'Argentina')
one_person.person_skill('Python')
person_two = Person('Rodri', 15, 'Argentina')
one_person.introduce()
person_two.introduce()