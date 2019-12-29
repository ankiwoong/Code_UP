import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

startAlphabet, endAlphabet = map(ord, input().split())

for i in range(startAlphabet, endAlphabet + 1):
    print(chr(i), end=' ')
