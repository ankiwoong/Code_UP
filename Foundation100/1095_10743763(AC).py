import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

n1 = int(input())
n2 = map(int, input().split())

arr = []
min_arr = []

for i in n2:
    arr.append(i)

for j in range(n1):
    min_arr.append(arr[j])

print(min(min_arr))
