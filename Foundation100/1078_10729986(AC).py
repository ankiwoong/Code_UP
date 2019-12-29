import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

n1 = int(input())

sum_i = 0

for i in range(n1 + 1):
    if i % 2 == 0:
        sum_i += i

print(sum_i)
