import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

n1, n2, n3 = map(int, input().split())

print(min(n1, n2, n3))
