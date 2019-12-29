import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

s1 = input()

s1_10 = int(s1, 16)

for i in range(1, 16):
    print('{0}*{1}={2}'.format(hex(s1_10)[2:].upper(), hex(i)[2:].upper(),hex(s1_10 * i)[2:].upper()))
