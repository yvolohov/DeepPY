
# single-line comment
def helloWorld():
    print('Hello world !!!')

def helpFunction():
    help('print')

def formatFunction():
    print('My name is {0} {1}'.format('Yaroslav', 'Volohov'))
    # 0 and 1 is order number of format() function arguments

def variables():
    _v1 = 1
    _2 = 2.233
    v3 = 3.0E-2
    _four = 'some value'
    print('{}, {}, {}, {}'.format(_v1, _2, v3, _four))

def codeLines():
    a = 1; b = 2; c = 3
    # symbol ; used as divider between operations on single line
    print(a + b + c)
    s = 'very long ' \
        'string'
    # one operation on several lines
    print(s)

# helloWorld()
# helpFunction()
# formatFunction()
# variables()
# codeLines()
