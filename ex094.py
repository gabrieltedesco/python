d = {}
l = []
r = ''
p = s = 0
m = []
v = []
while True:
    d['nome'] = input('Nome: ')
    d['idade'] = int(input('Idade: '))
    d['sexo'] = input('Sexo:[M/F]').upper()
    l.append(d.copy())
    p += 1
    s += d['idade']
    if d['sexo'] == 'F':
        m.append(d['nome'])
    d.clear()
    r = input('Quer continuar?[S/N] ').upper()
    if r == 'N':
        break
for c in l:
    if c['idade'] >= s/p:
        v.append(c['nome'])
print(f'Total de pessoas: {p}. A média do grupo: {s/p:.2f}')
print(f'Lista das mulheres: {m}')
print(f'Lista dos acima da média: {v}')
