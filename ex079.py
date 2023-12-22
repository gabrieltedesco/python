lista = []
n = 0
r = ''
while True:
    n = int(input('Valor: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado!')
    else:
        print('Valor repetido!')
    r = input('Quer continuar?[S/N]').upper()
    if r == 'N':
        break
print(sorted(lista))
