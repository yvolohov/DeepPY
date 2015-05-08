__author__ = 'yvolohov'

class Container():
    value = 0

    def set_class_var(self, value):
        Container.value = value

    def set_object_var(self, value):
        self.value = value

    def get_class_var(self):
        return Container.value

    def get_object_var(self):
        return self.value

c1 = Container()
c1.set_class_var(5)
c1.set_object_var(5)

c2 = Container()
c2.set_class_var(8)
c2.set_object_var(8)

print(c1.get_class_var()) #8
print(c1.get_object_var()) #5
print(c2.get_class_var()) #8
print(c2.get_object_var()) #8
