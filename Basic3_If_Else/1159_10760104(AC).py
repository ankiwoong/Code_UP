import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

n = int(input())

if 50 <= n <= 70:
    print('win')
elif n % 6 == 0:
    print('win')
else:
    print('lose')
