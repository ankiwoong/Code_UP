import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

n1 = int(input())

n1_16 = '{:#x}'.format(n1)

print(n1_16[2:])
