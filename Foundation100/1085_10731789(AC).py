import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

h, b, c, s = map(int, input().split())

sik = h * b * c * s/8/1024/1024

print('{0} MB'.format(round(sik, 1)))
