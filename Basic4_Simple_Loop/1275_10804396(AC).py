import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

n, k = map(int, input().split())

result = 1

for i in range(0, k):
    result *= n

print(result)
