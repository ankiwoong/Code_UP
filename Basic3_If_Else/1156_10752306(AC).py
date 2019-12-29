import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

n = int(input())

if n % 2 == 0:
    print('even')
else:
    print('odd')
