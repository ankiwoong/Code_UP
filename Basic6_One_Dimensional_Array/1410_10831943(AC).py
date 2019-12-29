import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

s = str(input())

open = s.count('(')
close = s.count(')')

print(open, close)
