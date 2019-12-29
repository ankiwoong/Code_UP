import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

n1 = int(input())

n1_8 = '{:#o}'.format(n1)

print(n1_8[2:])
