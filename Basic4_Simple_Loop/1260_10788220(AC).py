import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

n = list(map(int, input().split()))

sum = 0

for i in range(n[0], n[1] + 1):
    if i % 3 == 0:
        sum += i

print(sum)
