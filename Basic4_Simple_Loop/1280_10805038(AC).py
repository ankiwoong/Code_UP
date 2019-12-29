import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

a, b = map(int, input().split())

result = 0

for i in range(a, b + 1):
    if i % 2 == 0:
        print('-' + str(i), end='')
        result -= i
    else:
        print('+' + str(i), end='')
        result += i

print('=' + str(result))
