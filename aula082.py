def soma(x, y):
    return x+y
#Cuidado com o objeto None para o map quando a função não retorna valor (x % 2)

#ZIP
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = [7, 8, 9]
n = dict(zip(lista1, lista2))
m = list(zip(lista1, lista2, lista3))
print(n)
print(m)
#MAP
l1 = [x**2 for x in range(4)]
l2 = list(map((lambda x: x**2), range(4)))
print(l1)
print(l2)
#
l3 = list(map((lambda x, y: x+y), range(4), l2))
l4 = list(map(soma, range(4), l2))
print(l3)
print(l4)
#FILTER
l5 = list(filter((lambda x: x%2==0), range(5)))
print(l5)
#Listas comprimida vs. map+filter
l6 = [x**2 for x in range(5) if x%2==0]
l7 = list(map((lambda x: x**2), filter((lambda x: x%2==0), range(5))))
print(l6)
print(l7)
