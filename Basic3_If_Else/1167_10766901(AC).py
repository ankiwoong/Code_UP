import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

n = map(int, input().split())

list_n = list(n)
list_n.sort()

print(list_n[1])
