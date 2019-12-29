import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

n1 = input()

n1_16 = '0x' + n1

n1_10 = int(n1_16, 16)

print('{:#o}'.format(n1_10)[2:])
