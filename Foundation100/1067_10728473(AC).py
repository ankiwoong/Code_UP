import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

n1 = input()

if n1[0] == '-':
    print('minus')
    if int(n1) % 2 == 0:
        print('even')
    else:
        print('odd')
else:
    print('plus')
    if int(n1) % 2 == 0:
        print('even')
    else:
        print('odd')
