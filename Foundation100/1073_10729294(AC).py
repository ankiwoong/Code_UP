import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
n1 = map(int, input().split())
n1_list = list(n1)

for i in n1_list:
    if i != 0:
        print(i)
    else:
        break
