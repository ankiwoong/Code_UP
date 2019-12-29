import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

height, weight = map(float, input().split())

stdWeight = (height - 100) * 0.9
bmi = (weight - stdWeight) * 100 / stdWeight

if bmi <= 10:
    print('정상')
elif bmi <= 20:
    print('과체중')
else:
    print('비만')
