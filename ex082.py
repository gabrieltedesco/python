lista = []
lpares = []
limpares = []
n = 0
r = ''
while True:
    n = int(input('Valor: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado!')
        if n % 2 == 0:
            lpares.append(n)
        else:
            limpares.append(n)
    else:
        print('Valor repetido!')
    r = input('Quer continuar?[S/N]').upper()
    if r == 'N':
        break
print(sorted(lista))
print(sorted(lpares))
print(sorted(limpares))
