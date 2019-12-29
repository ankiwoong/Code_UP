import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

n1, n2 = map(int, input().split())

menu = [0, 400, 340, 170, 100, 70]

sum_calores = menu[n1] + menu[n2]

if sum_calores > 500:
    print('angry')
else:
    print('no angry')
