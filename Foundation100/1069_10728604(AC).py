﻿import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

n1 = input()

if n1 =='A':
    print('best!!!')
elif n1 == 'B':
    print('good!!')
elif n1 == 'C':
    print('run!')
elif n1 == 'D':
    print('slowly~')
else:
    print('what?')
