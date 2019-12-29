import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

n1 = int(input())

sum = 0
i = 1

while sum < n1:
    sum += i
    i += 1

print(sum)
