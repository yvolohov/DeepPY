import sys

if len(sys.argv) < 2:
    print(0)
    sys.exit()

pos = int(sys.argv[1])

if pos < 0:
    print(0)
elif pos == 0 or pos == 1:
    print(pos)
else:
    first = 0
    second = 1
    result = 0
    for i in range(2, pos + 1):
        result = first + second
        first = second
        second = result
    print(result)



# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144