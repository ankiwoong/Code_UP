import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

s1, s2 = input().split()

print(str(s2), str(s1))
