import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

s = list(input())

for i in s:
    pass_1 = ord(i) + 2
    print(chr(pass_1), end='')
    
print()

for j in s:
    pass_2 = ((ord(j) * 7) % 80 + 48)
    print(chr(pass_2), end='')
