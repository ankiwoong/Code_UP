import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

n1 = input()

n1_8 = '0o' + n1

print(int(n1_8, 8))
