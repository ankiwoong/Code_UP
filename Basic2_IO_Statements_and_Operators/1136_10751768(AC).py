import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

a, b = map(int, input().split())

if a == b:
    print(1)
else:
    print(0)
