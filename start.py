import sys

if len(sys.argv) < 2:
    print 0
    exit()

count = int(sys.argv[1])

def fibo(count):
        first = 0
        second = 1
        current = 0

        for i in range(count):
            current = first + second
            first = second
            second = current

        print current

fibo(10)

