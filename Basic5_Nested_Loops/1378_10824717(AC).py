import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

n = int(input())
result = 0
addNumober = 0

for i in range(1, n + 1):
    addNumober += i
    result += addNumober

print(result)
