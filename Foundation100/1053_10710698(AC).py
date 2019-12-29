import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

n1 = int(input())

if not n1 == True:
    print(1)
else:
    print(0)
