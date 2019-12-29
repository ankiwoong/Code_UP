import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

n1, n2 = map(int, input().split())

if n1 or n2 == True:
    print(1)
else:
    print(0)
