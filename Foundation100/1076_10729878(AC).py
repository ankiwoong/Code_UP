import io, sys
import string
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

a = list(string.ascii_lowercase)
s = input()

s_i = a.index(s)

print(' '.join(a[:s_i + 1]))
