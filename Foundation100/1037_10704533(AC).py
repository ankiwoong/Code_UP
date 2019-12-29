import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

ascii_n = input()

print(chr(int(ascii_n)))
