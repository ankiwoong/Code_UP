import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

string = list(input())

if len(string) == 3:
    if string[0] + string[1] + string[2] == 'IOI':
        print('IOI is the International Olympiad in Informatics.')
    else:
        print('I don\'t care.', end='')
else:
    print('I don\'t care.', end='')
