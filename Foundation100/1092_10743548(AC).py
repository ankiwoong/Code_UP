﻿import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

a, b, c = map(float, input().split())

d = 1

while (d % a != 0 or d % b != 0 or d % c != 0):
    d += 1

print(d)
