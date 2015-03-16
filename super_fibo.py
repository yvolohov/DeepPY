
def super_fibonacci(n, m):

    if not n > 0:
        return 0

    list = []

    for i in range(m):
        list.append(1)

    if n <= m:
        return list[n - 1]

    start = 0
    end = m
    count = n - m

    for i in range(count):
        number = 0

        for j in range(start, end):
            number += list[j]

        start += 1
        end += 1
        list.append(number)

    return list[n - 1]


print(super_fibonacci(9, 3))