import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

int_value = input()

list_int = []

for i in int_value:
    list_int.append(i)
    

print('[{0}]'.format(int(list_int[0]) * 10000))
print('[{0}]'.format(int(list_int[1]) * 1000))
print('[{0}]'.format(int(list_int[2]) * 100))
print('[{0}]'.format(int(list_int[3]) * 10))
print('[{0}]'.format(int(list_int[4]) * 1))
