import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

n1 = list(map(int, input().split()))
n = int(input())

print(n1[n - 1])
