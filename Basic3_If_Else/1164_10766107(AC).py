﻿import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')


n1, n2, n3 = map(int, input().split())

if n1 <= 170:
    print('CRASH')
elif n2 <= 170:
    print('CRASH')
elif n3 <= 170:
    print('CRASH')
else:
    print('PASS')
