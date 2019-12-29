import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

num = int(input())

for i in range(1, num + 1):
    print(i, end=' ')
