import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

n = input().split(" ")

n_list = []

for i in n:
    n_list.append(float(i))

n_list.sort()

while True:
    if n_list[0] == n_list[1]:
        print('%.2f' % n_list[0])
        break
    print('%.2f' % n_list[0], end=' ')
    n_list[0] = round(n_list[0] + 0.01, 2)
