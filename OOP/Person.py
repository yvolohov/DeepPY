__author__ = 'yvolohov'

class Person:

    # constructor
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    # setter
    def set_name(self, new_name):
        self.name = new_name

    def print_full_name(self):
        print(self.name + ' ' + self.surname)

def test_person():
    bob = Person('Bob', 'Smith')
    john = Person('John', 'Taylor')
    bob.print_full_name()
    john.print_full_name()
    bob.set_name('Robert')
    bob.print_full_name()