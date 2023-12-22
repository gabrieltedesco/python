tupla = (int(input('Digite um valor: ')), int(input('Digite um valor: ')),
         int(input('Digite um valor: ')), int(input('Digite um valor: ')))
print(f'Foram digitados {tupla.count(9)} valores 9')
if 3 in tupla:
    print(f'O valor 3 está na {tupla.index(3) +1}° posição')
else:
    print('O valor 3 não está na tupla')
print(f'Foram digitados os pares: ', end='')
for n in tupla:
    if n % 2 == 0:
        print(f'{n} ', end='')
