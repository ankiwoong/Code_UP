import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

hour, min = input().split(':')

print(hour + ':' + min)
