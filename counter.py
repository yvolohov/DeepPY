
def counter(a, b):
    sa = str(a)
    sb = str(b)
    sta = set(sa)
    stb = set(sb)
    count = 0

    for i in stb:
        if i in sta:
           count += 1

    return count

print(counter(123, 45))
