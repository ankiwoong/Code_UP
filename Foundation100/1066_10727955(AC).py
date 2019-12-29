import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

n1, n2, n3 = map(int, input().split())

for i in n1, n2, n3:
    if i % 2 == 0:
        print('even')
    else:
        print('odd')
