l = []
g = []
r = magro = gordo = 0
while True:
    g.append(input('Nome: '))
    g.append(int(input('Peso: ')))
    l.append(g[:])
    g.clear()
    r = input('Quer continuar?[S/N]').upper()
    if r == 'N':
        break
for p in l:
    if p[1] <= 70:
        magro += 1
    elif p[1] >= 100:
        gordo += 1
print(f'Há {magro} pessoas magras e {gordo} pessoas gordas')
