n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
op = 0
while True:
    print('''=================
    MENU
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair''')
    op = int(input('Sua opção: '))
    if op == 1:
        print(f'A soma de {n1} e {n2} vale {n1+n2}')
    if op == 2:
        print(f'A multiplicação de {n1} e {n2} vale {n1*n2}')
    if op == 3:
        if n1 > n2:
            print(f'O maior valor é {n1}')
        else:
            print(f'O maior valor é {n2}')
    if op == 4:
        n1 = int(input('Digite outro valor para o primeiro: '))
        n2 = int(input('Digite outro valor para o segundo: '))
    if op == 5:
        print('Finalizando o programa!')
        break

while var not c:
