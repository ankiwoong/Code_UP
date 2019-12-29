import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

f1 = input()

print('%.2f'%float(f1))
