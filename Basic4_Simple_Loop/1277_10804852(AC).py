import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

n = int(input())
n1 = list(map(int, input().split()))

if n == len(n1):
    print(n1[0], n1[len(n1)//2], n1[-1])
else:
    pass
