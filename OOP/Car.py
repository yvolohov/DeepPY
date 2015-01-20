__author__ = 'yvolohov'

class Car:

    # constructor
    def __init__(self, model):
        self.model = model

    # string representation of the object
    def __str__(self):
        return 'Car, model: ' + self.model

def test_car():
    bmw = Car('BMW')
    nissan = Car('Nissan')
    print bmw
    print nissan