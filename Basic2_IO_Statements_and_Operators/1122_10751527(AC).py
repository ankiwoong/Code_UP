import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

n = int(input())

sec = n % 60
min = int(n / 60 % 60)

print(min, sec)
