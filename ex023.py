n = int(input('Digite um número até 9999: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print(f' Unidades: {u} \n Dezenas: {d} \n Centenas: {c} \n Milhares: {m}')
