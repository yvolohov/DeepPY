__author__ = 'yvolohov'

#"Parent" is module name and class name
from Parent import Parent

class Child(Parent):
    def __str__(self):
        return Parent.__str__(self) + ' -> Child'