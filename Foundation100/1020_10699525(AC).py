import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

code1, code2 = input().split('-')

print(code1 + code2)
