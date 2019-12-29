import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

y, m, d = map(int,input().split())

n = (y + m + d) % 1000
n = int(n / 100)

if n % 2 == 0:
    print('대박')
else:
    print('그럭저럭')
