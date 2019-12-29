import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

w, h, b = map(int, input().split())

sik = w * h * b / 8 / 1024 / 1024

print('%.2f MB'%sik)
