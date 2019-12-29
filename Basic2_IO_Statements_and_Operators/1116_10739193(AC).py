import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

import math

a, b = map(int, input().split())

print('{0}+{1}={2}'.format(a, b, a + b))
print('{0}-{1}={2}'.format(a, b, a - b))
print('{0}*{1}={2}'.format(a, b, a * b))
print('{0}/{1}={2}'.format(a, b, math.floor(a / b)))
