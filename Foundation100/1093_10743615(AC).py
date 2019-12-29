import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

n1 = int(input())
n2 = map(int, input().split())

n2_list = list(n2)
arr = []

for i in range(24):
    arr. append(0)
for i in range(n1):
    arr[n2_list[i]] += 1
for i in range(1, 24):
    print(arr[i], end=' ')
