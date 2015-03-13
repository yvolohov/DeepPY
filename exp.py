import sys
import math

if len(sys.argv) < 4:
    print(0)
    sys.exit()

arg1 = float(sys.argv[1])
arg2 = float(sys.argv[2])
arg3 = float(sys.argv[3])

result1 = (1 / (arg3 * math.sqrt(2 * math.pi)))
result2 = ((arg1 - arg2) ** 2) / (2 * (arg3**2))
result = round(result1 * math.exp(-result2), 11)

print(result)