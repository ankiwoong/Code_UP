﻿import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

n, m = map(int, input().split())

for i in range(0, m):
    if i == 0 or i == m- 1:
        for j in range(0, n):
            if j == 0 or j == n-1:
                print('+', end='')
            else:
                print('-', end='')
        print()
    else:
        for j in range(0, n):
            if j==0 or j==n-1:
                 print('|', end ='')
            else:
                 print(' ', end='')
        print()
