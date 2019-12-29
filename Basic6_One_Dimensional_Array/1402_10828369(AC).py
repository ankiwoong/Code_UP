import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

n = int(input())
n_list = list(map(int, input().split()))

n_list.reverse()

if n == len(n_list):
    for i in n_list:
        print(i, end=' ')
else:
    pass
