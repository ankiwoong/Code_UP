import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

n = int(input())

sum = 0

for i in range(1, n + 1):
    sum += i

print(sum)
