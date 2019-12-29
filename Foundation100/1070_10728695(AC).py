import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

n1 = int(input())

if n1 == 12 or n1 == 1 or n1 == 2:
    print('winter')
elif n1 == 3 or n1 == 4 or n1 == 5:
    print('spring')
elif n1 == 6 or n1 == 7 or n1 == 8:
    print('summer')
elif n1 == 9 or n1 == 10 or n1 == 11:
    print('fall')
