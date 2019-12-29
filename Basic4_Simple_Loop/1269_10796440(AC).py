import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

a, b, c, n = list(map(int, input().split()))

for i in range(0, n - 1):
    a = a * b + c

print(a)
