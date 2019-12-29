import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

n = int(input())
n1 = list(map(int, input().split()))

if n == len(n1):
    for i in range(0, 2):
        for j in n1:
            print(j)
else:
    pass
