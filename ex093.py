d = {}
d['nome'] = input('Nome: ')
d['partidas'] = int(input('Partidas: '))
d['gols'] = []
t = 0
for c in range(0, d['partidas']):
    v = int(input(f'Gols na partida {c+1}: '))
    d['gols'].append(v)
    t += v
print(f'{d["nome"]} jogou {d["partidas"]} e marcou no total {t} gols')
