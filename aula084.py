def geraQuad1(x):
    for i in range(x):
        return i**2

l1 = geraQuad1(5)
print(l1)
#
def geraQuad2(x):
    for i in range(x):
        yield i**2

l2 = list(geraQuad2(5))
print(l2)
#Função fica parada até ser chamada para continuar a execução
l3 = geraQuad2(5)
print(l3.__next__())
print(l3.__next__())
print(l3.__next__())
print(l3.__next__())
print(list(l3))
