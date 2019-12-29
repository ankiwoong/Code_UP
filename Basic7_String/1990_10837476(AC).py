import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

n = int(input())

if n % 3 == 0:
    print(1)
else:
    print(0)
