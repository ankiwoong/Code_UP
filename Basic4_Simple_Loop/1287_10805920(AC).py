﻿import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

while True:
    n = int(input())
    if 1 <= n <= 9:
        break

for i in range(1, 10):
    for j in range(0, i * n):
        print('*', end='')
    print()
