from random import randint
c = j = p = 0
while True:
    c = randint(1, 10)
    print('''MENU
    [0] Par
    [1] Ímpar''')
    j = int(input('Sua escolha: '))
    if c % 2 == j:
        print('Acertou! \n')
        p += 1
    else:
        break
print(f'Sua pontuação consecutiva foi {p} acertos')
