
""" Private data, Getters and Setters"""

class PrivateBox:
    def __init__(self, key, value):
        self.__key = key     # we use '__str' to set data privacy
        self.__value = value
    def access_key(self, key):
        return self.__key == key
    # We use getters to obtain data
    def get_key(self):
        return self.__key
    def get_value(self, key):
        if self.access_key(key):
            return self.__value
        else:
            print("The key entered is incorrect.")
    # We use setters to stablish data to private data
    def set_key(self, new_key, key):
        if self.access_key(key):
            if len(new_key) < 4:
                print('The key must have at least 4 characters.')
            else:
                self.__key = new_key
        else:
            print("The key entered is incorrect.")
    def set_value(self, new_value, key):
        if self.access_key(key):
            if new_value <= 0:
                print('It has not entered into positive value.')
            else:
                self.__value = new_value
        else:
            print("The key entered is incorrect.")

box = PrivateBox('4000', 5000)
box.set_key('ass', '4000')
print(box.get_key())
