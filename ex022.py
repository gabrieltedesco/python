n = input('Digite seu nome completo: ')
n1 = n.strip()
m = n1.count(' ')
print('='*12)
print(f'Nome: {n.strip()}')
print(f'O número de letras é: {len(n1) - m}')
lista = n1.split()
print(f'O seu primeiro nome é: {lista[0]}')
