import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

ascii_s = input()

print(ord(ascii_s))
