lista = []
for c in range(0, 5):
    lista.append(int(input('Digite um valor: ')))
print(f'O maior valor é {max(lista)} é sua posição é {lista.index(max(lista)) + 1}°')
