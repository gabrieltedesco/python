n = input('Digite seu nome completo: ').strip()
lista = n.split()
c = n.count(' ')
print(f'Seu primeiro nome é {lista[0]} e seu último nome é {lista[c]}')
