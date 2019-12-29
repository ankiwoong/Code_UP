import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

n = int(input())

for i in range(1, n + 1):
    for j in range(0, n):
        print(i + j * n, end=' ')
    print()
