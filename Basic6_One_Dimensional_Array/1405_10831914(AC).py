import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

import collections

n = int(input())
n1 = list(map(int, input().split()))
n1 = collections.deque(n1)

n1.rotate(1)

for i in range(0, n):
    n1.rotate(-1)
    for j in n1:
        print(j, end=' ')
    print()
