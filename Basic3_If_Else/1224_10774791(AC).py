import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

n = list(map(int, input().split()))

if n[0] / n[1] > n[2] / n[3]:
    print('>')
elif n[0] / n[1] == n[2] / n[3]:
    print('=')
else:
    print('<')
