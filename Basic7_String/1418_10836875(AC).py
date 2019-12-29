import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

string = input()

for i in range(0, len(string)):
    if string[i] == 't':
        print(i+1, end=' ')
