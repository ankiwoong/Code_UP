import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

year, mon, day = input().split('.')
print(year.zfill(4) + '.' + mon.zfill(2) + '.' + day.zfill(2))
