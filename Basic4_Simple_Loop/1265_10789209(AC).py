import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

n = int(input())

for i in range(1, 10):
    print('{0}*{1}={2}'.format(n, i, n * i))
