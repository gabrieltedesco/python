n = int(input('Digite um valor: '))
f = 1
c = n
while c != 1:
    f *= c
    c -= 1
print(f'O fatorial de {n} vale {f}')
