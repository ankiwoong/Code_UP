import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

s1 = input().split()

s1_list = list(s1)

last = s1_list.index('q')

for i in s1_list[:last + 1]:
    print(i)
