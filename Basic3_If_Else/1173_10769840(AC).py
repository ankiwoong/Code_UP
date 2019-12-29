import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

hour, min = map(int, input().split())

if min - 30 < 0:
    min = 60 + (min - 30)
    if hour -1 < 0:
        hour = 23
    else:
        hour -= 1
else:
    min -= 30

print(str(hour) + ' ' +str(min))
