import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

h, w = input().split()

h, w = int(h), int(w)

m=[]

for i in range(h):
    m.append([])
    for j in range(w) :
        m[i].append(0)

n = int(input())

for i in range(n):
    l, d, x, y = input().split()
    for j in range(int(l)):
        if(int(d) == 0):
            m[int(x) - 1][int(y) - 1 + j] = 1
        else:
            m[int(x) - 1 + j][int(y) - 1] = 1

for i in range(h):
    for j in range(w):
        print(m[i][j], end=' ')
    print()