a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
c = 1
print(f'{a1}', end=' ')
while c < 10:
    print(a1 + r*c, end=' ')
    c += 1
