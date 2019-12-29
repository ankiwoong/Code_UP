import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

n1 = int(input())

if n1 >= 90:
    print('A')
elif n1 >= 70:
    print('B')
elif n1 >= 40:
    print('C')
else:
    print('D')
