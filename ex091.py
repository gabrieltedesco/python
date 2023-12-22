from random import randint
d = {}
l = []
ord = []
nord = []
for c in range(0, 4):
    d['nome'] = input('Seu nome: ')
    d['valor'] = randint(1, 6)
    print('Número sorteado!')
    ord.append(d['valor'])
    l.append(d.copy())
    d.clear()
print(ord)
ord.sort(reverse=True)
print(f'{"RANKING":=^30}')
for k, c1 in enumerate(ord):
    for c2 in l:
        if c2['valor'] == c1 and c2['nome'] not in nord:
            nord.append(c2['nome'])
            print(f'{k+1}° lugar - {c2["nome"]} - {c2["valor"]} pontos')
            break
