import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

a = -2147483648
b = 2147483647

print(a, b)
