import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

s1 = list(input())
s2 = list(input())
s3 = list(input())

if s1[-1] == s2[0] and s2[-1] == s3[0] and s3[-1] == s1[0]:
    print('good')
else:
    print('bad')
