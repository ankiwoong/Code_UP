import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
n = int(input())
n1 = list(map(int, input().split()))

n1.sort()

if n == len(n1):
    print(max(n1))
else:
    pass
