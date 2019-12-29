import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

n1 = int(input())


for i in range(n1 + 1):
    if i % 3 == 0:
        pass
    else:
        print(i, end=' ')
