""" Inheritance allows us to define a class that
    inherits all the methods and properties from parent class. """

""" Parent Class (upper class) """
class Cars():
    def __init__(self, brand, model, motor):
        self.brand = brand
        self.model = model
        self.motor = motor == False
        #self.structure = ''
    def status(self):
        if self.motor:
            print('The engine is off.')
        else:
            print('The is on')
    def introduce(self): # we use for Polymorphism
        print(f'This car, {self.brand}, is the model {self.model} and its structure is {self.structure}')

""" Derived Class or Child (sub class) """
class Bus(Cars):
    def __init__(self, brand, model, motor):
        super().__init__(brand, model, motor)
        self.structure = 'integral'

class Sudan(Cars):
    def __init__(self, brand, model, motor):
        super().__init__(brand, model, motor)
        self.structure = 'uni body'
class PickUp(Cars):
    def __init__(self, brand, model, motor):
        super().__init__(brand, model, motor)
        self.structure = 'body on frame'
my_bus = Bus('Iveco', '1998', 'diesel')
my_bus.introduce() 
my_car = Sudan('Nissan', '2024', 'gasoline')
my_car.introduce() # these are examples of Polymorphism
""" We can use super() built-in function or the parent name Cars to
    automatically inherit the methods and properties from its parent.
    In the example above we override the parent method. """
""" Polymorphism is the ability of a method to do different things."""