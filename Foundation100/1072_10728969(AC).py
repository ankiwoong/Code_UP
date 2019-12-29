import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

n1 = int(input())
n2 = map(int, input().split())

n2_list = list(n2)

for i in n2_list:
    if n1 < len(n2_list):
        break
    else:
        print(i)
