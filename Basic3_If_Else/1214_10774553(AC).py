import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

import calendar

n1, n2 = map(int, input().split())

a = calendar.monthrange(n1, n2)
print(a[1])
