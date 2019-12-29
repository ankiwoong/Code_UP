import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

n = int(input())

a = oct(n)
b = hex(n)

print(a[2:], b[2:].upper())
