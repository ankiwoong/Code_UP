import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

n1, n2 = map(int, input().split())

for i in range(n1, n2 + 1):
    for j in range(1, 10):
        print('{0}*{1}={2}'.format(i, j, i*j))
