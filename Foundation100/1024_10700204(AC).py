import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

str_value = input()

for s in str_value:
    print('\'{0}\''.format(s))
