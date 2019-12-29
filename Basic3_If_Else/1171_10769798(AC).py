import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

g1, g2, g3 = input().split()

g2 = int(g2)
g3 = int(g3)

if g2 < 10:
    g2 = '0' + str(g2)

if g3 < 10:
    g3 = '00' + str(g3)
elif g3 < 100:
    g3 = '0' + str(g3)

sn = g1 + str(g2) + str(g3)
print(sn)
