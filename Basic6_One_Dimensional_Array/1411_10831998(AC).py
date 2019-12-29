import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

n = int(input())

cards = []
miss = []

for i in range(1, n + 1):
    cards.append(i)

for i in range(0, n - 1):
    n1 = int(input())
    miss.append(n1)

for card in miss:
    cards.remove(card)

print(cards[0])
