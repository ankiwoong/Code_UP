﻿import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

no_advertise, advertise, advertise_cost = map(int, input().split())

if(advertise - advertise_cost == no_advertise):
    print('does not matter')
elif(advertise - advertise_cost > no_advertise):
    print('advertise')
else:
    print('do not advertise')
