import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

import string

text = input()

s = string.ascii_lowercase
list_s = []

for i in s:
    list_s.append(i)

for j in range(0, len(list_s)):
    print('{0}:{1}'.format(list_s[j], text.count(list_s[j])))
