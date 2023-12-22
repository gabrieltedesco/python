s = ''
i = 0
r = 'S'
a = b = c = 0
while True:
    s = input('Sexo [M/F]: ').upper()
    i = int(input('Idade: '))
    if i >= 18:
        a += 1
    if s == 'M':
        b += 1
    if s == 'F' and i < 20:
        c += 1
    r = input('Quer continuar?[S/N] ').upper()
    if r == 'N':
        break
    print('='*16)
print('='*25)
print(f'''Resultado:
Pessoas com mais de 18: {a}
Homens cadastrados: {b}
Mulheres com menos de 20: {c}''')
