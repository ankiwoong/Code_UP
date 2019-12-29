import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

map = []

for i in range(19) :
    map.append(input().split())

n = int(input())

for i in range(n):
    x, y = input().split()
    x, y = int(x) - 1, int(y) - 1
    for j in range(19):
        if(map[j][y] == '0'):
            map[j][y] = '1'
        else:
            map[j][y] = '0'
        if(map[x][j] == '0'):
            map[x][j] = '1'
        else:
            map[x][j] = '0'

for i in range(19):
    for j in range(19) :
        print(map[i][j], end = ' ')
    print()
