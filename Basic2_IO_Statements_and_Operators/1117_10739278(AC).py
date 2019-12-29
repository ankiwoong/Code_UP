import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

a, b = map(float, input().split())

print(round(a * b, 2))
