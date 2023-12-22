l = [[], [], []]
par = terc = maior = 0
for p in range(0, 3):
    for c in range(0, 3):
        n = int(input(f'Digite um valor para a casa [{p}, {c}]: '))
        if n % 2 == 0:
            par += n
        if c == 2:
            terc += n
        if p == 1 and n >= maior:
            maior = n
        l[p].append(n)
print(f'[{l[0][0]:^5}] [{l[0][1]:^5}] [{l[0][2]:^5}]')
print(f'[{l[1][0]:^5}] [{l[1][1]:^5}] [{l[1][2]:^5}]')
print(f'[{l[2][0]:^5}] [{l[2][1]:^5}] [{l[2][2]:^5}]')
print(f'A soma dos pares é {par}, a soma da terceira coluna é {terc} e o maior da segunda linha é {maior}')
