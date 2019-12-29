import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

import math

current_time, score_class_1, score_class_2 = map(int, input().split())

additional_points = (90 - current_time) / 5
additional_points = math.ceil(additional_points)
score_class_1 += additional_points

if(score_class_1 > score_class_2):
    print('win')
elif(score_class_1 < score_class_2):
    print('lose')
else:
    print('same')
