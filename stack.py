import sys

if len(sys.argv) < 2:
    print('')
    sys.exit()

arg = sys.argv[1]
length = len(arg)
stack = 0
result = True

for i in range(length):
    if arg[i] == '(':
        stack += 1
    elif arg[i] == ')':
        stack -= 1

    if stack < 0:
        result = False
        break

if stack != 0:
    result = False

if result:
    print('YES')
else:
    print('NO')



