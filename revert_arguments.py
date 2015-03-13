import sys

if len(sys.argv) < 2:
    print('')
    sys.exit()

length = len(sys.argv)
result = ''

for i in range(1, length):
    result += sys.argv[length - i]

    if i < length - 1:
        result += ' '

print(result)