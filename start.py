import sys

if len(sys.argv) < 2:
    print('')
    exit()

st = sys.argv[1]
st = st.replace(' ', '')
st = st.upper()

print(st)

