import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

n = list(map(int, input().split()))
n.sort()

if n[2] < n[0] + n[1]:
    print('yes')
else:
    print('no')
