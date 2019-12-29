import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

n = map(int, input().split())

list_i = []

for i in n:
    list_i.append(i)

sum = sum(list_i)

if sum == 1:
    print('도')
elif sum == 2:
    print('개')
elif sum == 3:
    print('걸')
elif sum == 4:
    print('윷')
else:
    print('모')
