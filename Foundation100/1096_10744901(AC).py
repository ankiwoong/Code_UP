import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

n = int(input())

m = [[0 for col in range(20)] for row in range(20)]

for i in range(n):
    x, y = input().split()
    m[int(x)][int(y)] = 1

for i in range(1, 20):
    for j in range(1, 20):
        print(m[i][j], end=' ')
    print('')
