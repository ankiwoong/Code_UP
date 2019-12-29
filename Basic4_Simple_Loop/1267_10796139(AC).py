import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

n = int(input())
n1 = list(map(int, input().split()))

if n == len(n1):
    sum = 0
    for i in n1:
        if i % 5 == 0:
            sum += i
    print(sum)
else:
    pass
