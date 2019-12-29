import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

n = list(map(int, input().split()))

for i in range(n[0], n[1] + 1):
    if i % 2 != 0:
        print(i, end=' ')
