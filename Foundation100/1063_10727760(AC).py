﻿import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

n1, n2 = map(int, input().split())

if n1 > n2:
    print(n1)
else:
    print(n2)
