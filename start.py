from random import randint

import first

def operatorsDiv():
    pow = 3 ** 3 # 27
    print('pow', pow)

    div1 = 7 / 3
    print('div1 {}'.format(div1))

    div2 = 7 // 3
    print('div2 {}'.format(div2))

    div3 = 7 % 3
    print('div3 {}'.format(div3))


def operatorIn():
    arr1 = [3, 4, 5, 6, 7]
    print(2 in arr1)
    print(6 in arr1)
    print(2 not in arr1)
    print(6 not in arr1)

def operatorIf():
    num = randint(0, 2)

    if num == 0:
        print('zero')
    elif num == 1:
        print('one')
    else:
        print('two')

def operatorWhile():
    counter = 0
    num = randint(10, 50)
    stars = '';

    while counter < num:
        stars += '*'
        counter += 1

    print(stars)


# operatorsDiv()
# operatorIn()
# operatorIf()
operatorWhile()
