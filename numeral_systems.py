
def convert_n_to_m(x, n, m):
    symbols = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    sys_symbols = symbols[0 : n]
    x = str(x).upper()

    if len(x) == 0:
        return False

    for i in range(len(x)):
        if x[i] not in sys_symbols:
            return False

    return True

print(convert_n_to_m('0', 0, 1))
