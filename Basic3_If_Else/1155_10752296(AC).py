import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

n = int(input())

if n % 7 == 0:
    print('multiple')
else:
    print('not multiple')
