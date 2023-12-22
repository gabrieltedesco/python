def fat(a=0):
    f = 1
    if a != 0:
        for c in range(a, 1, -1):
            f *= c
        return f


v = int(input('Digite um valor: '))
n = fat(v)
print(f'O fatorial de {v} é {n}')
