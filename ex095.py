l = []
d = {}
r = ''
l2 = []
while True:
    d['nome'] = input('Nome: ')
    d['partidas'] = int(input('Partidas: '))
    t = 0
    for c in range(0, d['partidas']):
        v = int(input(f'Gols na partida {c+1}: '))
        l2.append(v)
        t += v
    d['gols'] = l2.copy()
    d['total'] = t
    l.append(d.copy())
    l2.clear()
    d.clear()
    r = input('Quer continuar?[S/N] ').upper()
    if r == 'N':
        break
print(f'{"No.":<4}{"Nome":<10}{"Gols":<15}{"Total":<4}')
for k, v in enumerate(l):
    print(f'{k:<4}{v["nome"]:<10}{str(v["gols"]):<15}{v["total"]:<4}')
