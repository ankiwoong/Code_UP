import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

float_n1, float_n2 = input().split('.')

print(float_n1)
print(float_n2)
