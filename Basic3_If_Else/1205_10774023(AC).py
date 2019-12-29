import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

n1, n2 = map(float, input().split())

plus = n1 + n2; minus = n1 - n2; multiply = n1 * n2; division = n1 / n2; squared = n1 ** n2
plus2 = n2 + n1; minus2 = n2 - n1; multiply2 = n2 * n1; division2 = n2 / n1; squared2 = n2 ** n1

list_n = [plus, minus, multiply, division, squared, plus2, minus2, multiply2, division2, squared2]

print('%.6f'%max(list_n))
