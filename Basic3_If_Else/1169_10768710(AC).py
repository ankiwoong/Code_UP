import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

a = int(input())
b = 2012 - a + 1

if b < 2000:
    b = str(b)
    print(int(b[2:4]), 1)
else:
    b = str(b)
    print(int(b[2:4]), 3)
