import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

n1, n2 = map(int, input().split())

print(n1, n2)
