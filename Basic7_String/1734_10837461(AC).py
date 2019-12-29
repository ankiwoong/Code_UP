import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

id = input()

print('welcome! {0}'.format(id))
