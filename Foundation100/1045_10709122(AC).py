import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

def cal(n1, n2):
    print(n1 + n2)
    print(n1 - n2)
    print(n1 * n2)
    print(n1 // n2)
    print(n1 % n2)
    n = n1 / n2
    print('%.2f' % n)
    
n1, n2 = map(int,input().split())

cal(n1, n2)
