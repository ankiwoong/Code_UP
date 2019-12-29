import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

b, g = input().split()
g = int(g)
y = 2012

if g == 1:
    b = int('19' + b[0:2])
    print(y - b + 1)
elif g == 2:
    b = int('19' + b[0:2])
    print(y - b + 1)
elif g == 3:
    b = int('20' + b[0:2])
    print(y - b + 1)
else:
    b = int('20' + b[0:2])
    print(y - b + 1)
