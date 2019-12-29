import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

n = input().split()
n_list = list(n)

if int(n_list[2]) < 10:
    print('{0}{1}0{2}'.format(n_list[0], n_list[1], n_list[2]))
else:
    print(''.join(n_list))
