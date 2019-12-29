import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

n = int(input())

for i in range(1, n+1):
    for j in range(0, i):
        print('*', end='')
    print()

for i in range(n - 1, 0, -1):
    for j in range(0, i):
        print('*', end='')
    print()
