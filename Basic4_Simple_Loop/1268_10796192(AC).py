import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

n = int(input())
n1 = list(map(int, input().split()))

if n == len(n1):
    sum = []
    for i in n1:
        if i % 2 == 0:
            sum.append(i)
    print(len(sum))
else:
    pass
