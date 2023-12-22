m = 0
ve = ''
vei = 0
mu = 0
for c in range(0, 4):
    p = input('Nome: ')
    i = int(input('Idade: '))
    s = input('Sexo [M/F]: ').upper()
    m += i
    if s == 'M':
        if c == 0:
            ve = p
            vei = i
        if i >= vei:
            vei = i
            ve = p
    if s == 'F' and i < 20:
        mu += 1
print(f'''Resultados:
A média de idade do grupo é {m/4:.2f}
O nome do homem mais velho é {ve}
O número de mulheres com menos de 20 anos é {mu}
''')
