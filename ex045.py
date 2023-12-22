from random import randint
print('===== JOKENPÔ =====')
print('''Faça sua escolha,
[1] Pedra
[2] Papel
[3] Tesoura''')
p = int(input('Sua opção: '))
c = randint(1, 3)
p1 = 0
p2 = 0
if p == 1:
    p1 = 'Pedra'
elif p == 2:
    p1 = 'Papel'
elif p == 3:
    p1 = 'Tesoura'
if c == 1:
    p2 = 'Pedra'
elif c == 2:
    p2 = 'Papel'
elif c == 3:
    p2 = 'Tesoura'

if p == c:
    print(f'Os jogadores empataram, ambos jogaram {p1}')
elif p == 1 and c == 2 or p == 2 and c == 3 or p == 3 and c == 1:
    print(f'Você perdeu, o computador jogou {p2}')
elif p == 1 and c == 3 or p == 2 and c == 1 or p == 3 and c == 2:
    print(f'Você ganhou, o computador jogou {p2}')
