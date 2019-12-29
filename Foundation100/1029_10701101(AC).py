import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

float_value = input()

print('%.11f'%float(float_value))
