import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

n1 = int(input())

for i in range(1, n1 + 1):
    if i == 3 or i == 6 or i == 9:
        print('X',end=' ')
    else:
        print(i, end=' ')
