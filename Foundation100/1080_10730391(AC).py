import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

n1 = int(input())

i = 1
sum = 0

while True:
    sum += i
    if sum >= n1:
        print(i)
        break
    i += 1
