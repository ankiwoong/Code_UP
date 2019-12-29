import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

for i in range(1, 101):
    print(i, end=' ')
