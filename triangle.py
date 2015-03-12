import sys

if len(sys.argv) < 4:
    print "not triangle"

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

if a <= 0 or b <= 0 or c <= 0 or c >= a + b or b >= a + c or a >= b + c:
    print "not triangle"
else:
    print "triangle"
