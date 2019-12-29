import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

n = input()

a = n[1] + n[0]
a = int(a) * 2

if a > 99:
    a = a % 100

if a <= 50:
    print(a)
    print('GOOD')
else:
    print(a)
    print('OH MY GOD')
