import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

s = int(input())

h = 9 / 5 * s + 32

print('%.3f' % h)
