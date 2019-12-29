import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

n1 = int(input())

while n1 >= 1:
    print(n1)
    n1 = n1 - 1
