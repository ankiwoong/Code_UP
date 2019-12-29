import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

year, month, day = input().split('.')

print('{d}-{m}-{y}'.format(d=day, m=month, y=year))
