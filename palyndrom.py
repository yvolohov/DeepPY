import sys

if len(sys.argv) < 2:
    print('')
    exit()

st = sys.argv[1]
st = st.replace(' ', '')
st = st.upper()

length = len(st)
mn = 0
mx = length - 1
result = True

for i in range(length):
    if st[mn] != st[mx]:
        result = False
        break
    mn += 1
    mx -= 1

if result:
    print('YES')
else:
    print('NO')
