import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

word = input()
c = []

for char in word:
    if char.isalpha():
        if char.isupper():
            c.append(chr((ord(char) - ord('A') - 3) % 26 + ord('A')))
        else:
            c.append(chr((ord(char) - ord('a') - 3) % 26 + ord('A')))
    else:
        c.append(char)

print(''.join(c).lower())
