import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

s1 = input()

s1_ord = ord(s1)

print(chr(s1_ord + 1))
