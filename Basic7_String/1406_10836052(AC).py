import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

s = input()

if s == 'love':
    print('I love you.')
else:
    pass
