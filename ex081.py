lista = []
n = c = 0
r = ''
r1 = 'Não'
while True:
    n = int(input('Valor: '))
    if n not in lista:
        lista.append(n)
    else:
        print('Valor repetido!')
    c += 1
    if n == 5:
        r1 = 'Sim'
    r = input('Quer continuar?[S/N]').upper()
    if r == 'N':
        break
lista.sort(reverse=True)
print(lista)
print(f'Foram digitados {c} valores')
print(f'O cinco está na lista: {r1}')
