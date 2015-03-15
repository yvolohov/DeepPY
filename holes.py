def count_holes(n):
    import re

    if n == 0:
        return 1

    tp = str(n)
    regex = re.compile('^-{0,1}0{1,}$')

    if None != regex.match(tp):
        return 1

    regex = re.compile('^-{0,1}[0-9]{1,}$')

    if None != regex.match(tp):

        buffer = ''
        flag = False

        for i in range(len(tp)):

            if tp[i] in '123456789':
                flag = True

            if flag:
                buffer += tp[i]

        tp = buffer
        counter = 0

        for i in range(len(tp)):
            if tp[i] == '8':
                counter += 2
            elif tp[i] in ['0', '4', '6', '9']:
                counter += 1

        return counter

    else:
        return 'ERROR'

print(count_holes('-00000000100'))

