# set python v 2.x for using long

def convert_n_to_m(x, n, m):
    import math

    # if n or m are incorrect
    if n < 1 or n > 36 or m < 1 or m > 36:
        return False

    x = str(x).upper()

    # if empty string
    if len(x) == 0:
        return False

    symbols = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    sys_symbols = symbols[0 : n]
    length = len(x)

    # if x consists incorrect symbols
    for i in range(length):
        if x[i] not in sys_symbols:
            return False

    # from n to decimal system
    number10 = 0L

    if n > 1:
        for i in range(length):
            digit = x[length - i - 1]
            digit10 = sys_symbols.find(digit)
            number10 += (digit10 * long(math.pow(n, i)))
    else:
        number10 = len(x)

    # from decimal system to m
    if m > 1:
        r = long(number10 % m)
        q = long(number10 // m)
        result = symbols[r]

        while q > 0:
            r = q % m
            q = q // m
            result = symbols[r] + result
    else:
        result = '0' * number10

    return result

print(convert_n_to_m(123123123123123123123, 11, 16))