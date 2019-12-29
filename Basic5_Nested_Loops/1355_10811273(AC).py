import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

n = int(input())

for i in range(0, n):
    for j in range(0, i):
        print(' ', end='')
    for j in range(0, n - i):
        print('*', end='')
    print()
