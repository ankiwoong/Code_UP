import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

n1 = input()
print('{0} {0} {0}'.format(int(n1)))
