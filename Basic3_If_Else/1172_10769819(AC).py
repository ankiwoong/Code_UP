import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

n = map(int, input().split())

n_list = list(n)
n_list.sort()

for i in n_list:
    print(i, end=' ')
