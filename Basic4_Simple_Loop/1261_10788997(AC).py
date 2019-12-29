import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

n = list(map(int, input().split()))

isQuintuple = False

for i in n:
    if i % 5 == 0:
        print(i)
        isQuintuple = True
        break

if isQuintuple == False:
    print('0')
