lista = [x+10 for x in range(10)]
print(lista)

lista_2 = []
for c in range(0, 10):
    valor = c+10
    lista_2.append(valor)
print(lista_2)
#
lista_3 = [x for x in range(10) if x%3==0]
print(lista_3)

lista_4 = []
for c in range(0, 10):
    if c%3 == 0:
        lista_4.append(c)
print(lista_4)
#
lista_5 = [l1 + l2 for l1 in 'abc' for l2 in 'def']
print(lista_5)

lista_6 = []
for l1 in 'abc':
    for l2 in 'def':
        lista_6.append(l1 + l2)
print(lista_6) 
