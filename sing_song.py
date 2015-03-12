import sys

if len(sys.argv) < 4:
    print('')
    sys.exit()

x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])

if x <= 0 or y < 0 or (z != 0 and z != 1):
    print('')
    sys.exit()

cup = 'la-' * x
ls = len(cup) - 1
cup = cup[:ls] + ' '

cups = cup * y
ls = len(cups) - 1
cups = cups[:ls]

if z == 1:
    cups += '!'
else:
    cups += '.'

if y > 0:
    cups = ' ' + cups

print('Everybody sing a song:' + cups)