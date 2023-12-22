import moedas
v1 = float(input('Digite um valor: '))

print(f'Aumentando 10% de {v1} é {moedas.aumentar(v1, 10)}')
print(f'Diminuindo 10% de {v1} é {moedas.diminuir(v1, 10)}')
print(f'O dobro de {v1} é {moedas.dobro(v1)}')
print(f'A metade de {moedas.fmt(v1)} é {moedas.metade(v1, True)}')

moedas.resumo(v1, 10, 10)
