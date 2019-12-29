import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

k = int(input())

for i in range(1, 7):
    for j in range(1, 7):
        if i +j == k:
            print(i, j)
