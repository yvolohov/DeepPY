# only for python 2.x

class Sphere():

    r = 1
    x = y = z = 0

    def __init__(self, r = 1, x = 0, y = 0, z = 0):
        self.r = r
        self.x = x
        self.y = y
        self.z = z

    def get_volume(self):
        import math
        return (4.0 / 3) * math.pi * (self.r ** 3)

    def get_square(self):
        import math
        return 4 * math.pi * (self.r ** 2)

    def get_radius(self):
        return self.r

    def get_center(self):
        return (self.x, self.y, self.z)

    def set_radius(self, r):
        self.r = r

    def set_center(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def is_point_inside(self, x, y, z):
        import math
        distance = math.sqrt(((x - self.x)**2) + ((y - self.y)**2) + ((z - self.z)**2))
        return distance < self.r


sp = Sphere(0.5)
print(sp.is_point_inside(0, -1.5, 0))
sp.set_radius(1.6)
print(sp.is_point_inside(0, -1.5, 0))
