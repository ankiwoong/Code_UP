import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

n1, n2, n3 = map(int,input().split())

sum_n = n1 + n2 + n3
average_n = sum_n / 3

print(sum_n)
print('%.1f'%average_n)
