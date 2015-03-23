
class Student(object):

    def __init__(self, name, conf):
        self.name = name
        self.conf = conf
        self.exam = 0
        self.labs = []

        for i in range(self.conf['lab_num']):
            self.labs.append(0)

    def make_lab(self, m, n=None):

        if n is None:
            try:
                n = self.labs.index(0)
            except ValueError:
                return self
        elif not n < len(self.labs):
            return self

        if m > self.conf['lab_max']:
            self.labs[n] = self.conf['lab_max']
        else:
            self.labs[n] = m

        return self

    def make_exam(self, m):

        if m > self.conf['exam_max']:
            self.exam = self.conf['exam_max']
        else:
            self.exam = m

        return self

    def is_certified(self):
        s = self.exam

        for lab in self.labs:
            s += lab

        t = (s, (s / 100.0) >= self.conf['k'])
        return t

#conf1 = {'exam_max': 20,'lab_max': 40,'lab_num': 2,'k': 0.75}
#o1 = Student('Oleg', conf1)
#o1.is_certified()
#o2 = Student('Oleg', conf1)
#o2.make_lab(60).make_lab(35.2)
#o2.is_certified()
#o3 = Student('Oleg', conf1)
#o3.make_lab(10).make_lab(10).make_exam(15)
#print(o3.is_certified())
#o3.make_lab(20,1).make_lab(20,0)
#print(o3.is_certified())

conf2 = {'exam_max': 52,'lab_max': 8,'lab_num': 6,'k': 0.5}
o4 = Student('Oleg', conf2)
o4.make_exam(100)
print(o4.is_certified())