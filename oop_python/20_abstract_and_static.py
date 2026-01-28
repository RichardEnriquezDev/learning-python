### Abstract Base Class ###
""" Abstract Class: template or model of the classes that inherit it. """
from abc import ABC, abstractmethod

class Animal(ABC):
    animal_count = 0 # this is a static attribute
    def __init__(self, name):
        self.name = name
        Animal.animal_count += 1
    @abstractmethod
    def make_sound(self):
        pass
    @classmethod
    def get_animal_count(cls):
        print(f'The number of animal is: {cls.animal_count}')

# Derived Class
class Dog(Animal):
    def make_sound(self):
        print(f'My puppy {self.name} make sound Gua Gua!!')
class Cat(Animal):
    def make_sound(self):
        print(f'My kitten {self.name} make sound Miau Miau!!')

# Objects
puppy = Dog('Little Spot')
kitten = Cat('Fluff')
puppy.make_sound()
kitten.make_sound()
Animal.get_animal_count()