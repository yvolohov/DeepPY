
class SuperStr(str):

    def __init__(self, s):
        super(str, s)

    def is_repeatance(self, vs):

        if type(vs) != str:
            return False

        if len(self) == 0 or len(vs) == 0:
            return False

        if len(self) % len(vs) > 0:
           return False

        count = int(len(self) / len(vs))
        test_str = vs * count

        if self != test_str:
            return False

        return True

    def is_palindrom(self):

        st = self.upper()
        length = len(st)
        mn = 0
        mx = length - 1
        result = True

        for i in range(length):

            if st[mn] != st[mx]:
                result = False
                break

            mn += 1
            mx -= 1

        return result


s = SuperStr('123123123123')
print(s.is_repeatance('123')) # True
print(s.is_repeatance('123123')) # True
print(s.is_repeatance('123123123123')) # True
print(s.is_repeatance('12312')) # False
print(s.is_repeatance(123)) # False
print(s.is_palindrom()) # False
print(s) # 123123123123 (рядок)
print(int(s)) # 123123123123 (ціле число)
print(s + 'qwe') # 123123123123qwe
p = SuperStr('123_321')
print(p.is_palindrom()) # True