﻿import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

n, m = map(int, input().split())

for i in range(n - 1, -1, -1):
    for j in range(1, m + 1):
        print(i * m + j, end=' ')
    print()
