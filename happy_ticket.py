import sys

if len(sys.argv) < 3:
    print(0)
    sys.exit()

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
counter = 0

for i in range(num1, num2 + 1):
    st = str(i)
    ln = len(st)
    zeros = 6 - ln
    zst = '0' * zeros
    st = zst + st
    first = int(st[0]) + int(st[1]) + int(st[2])
    second = int(st[3]) + int(st[4]) + int(st[5])

    if first == second:
        counter += 1

print(counter)