import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

n1 = int(input())
n2 = map(int, input().split())

arr = []

for i in n2:
    arr.append(i)

arr.reverse()

for j in range(n1):
    print(arr[j], end =' ')
