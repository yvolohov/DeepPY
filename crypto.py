import sys

if len(sys.argv) < 2:
    print('')
    sys.exit()

key = 'aaaaabbbbbabbbaabbababbaaababaab'
alphabet = 'abcdefghijklmnopqrstuvwxyz'

sentence = sys.argv[1]
sentence = sentence.replace(' ', '')
length = len(sentence)

groups = []
buffer = ''

for i in range(length):

    if sentence[i].isupper():
        buffer += 'b'
    else:
        buffer += 'a'

    if (i + 1) % 5 == 0:
        groups.append(buffer)
        buffer = ''

result = ''

for group in groups:
    pos = key.find(group)
    result += alphabet[pos]

print(result)
