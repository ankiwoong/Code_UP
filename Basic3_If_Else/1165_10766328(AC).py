import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

t, s = map(int, input().split())

if t % 10 == 0:
    fs = s + (90 - t) / 5
else:
    fs = s + (90 - t) / 5 + 1

print(int(fs))
