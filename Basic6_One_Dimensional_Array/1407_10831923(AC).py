import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

s = list(map(str, input().split()))

print(''.join(s))
