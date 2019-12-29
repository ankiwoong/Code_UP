import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

n = int(input())
n1 = list(map(int, input().split()))

m = int(input())
m1 = list(map(int, input().split()))

n1_list = []

if n == len(n1):
    for i in n1:
        n1_list.append(i)
else:
    pass

if m == len(m1):
    for j in m1:
        if (j in n1_list) == True:
            print(1, end=' ')
        else:
            print(0, end=' ')
else:
    pass
