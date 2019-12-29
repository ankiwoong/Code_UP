import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

n = float(input())

if n >= 50 and n <= 60:
    print('win')
else:
    print('lose')
