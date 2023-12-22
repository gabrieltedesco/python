from random import randint
def sorteio(var):
    """
    → Faz o sorteio de 5 valores aleatórios
    :param var: lista que recebe os valores sorteados
    :return: sem retorno
    """
    for c1 in range(0, 5):
        var.append(randint(1, 10))
def somapar(var, var2):
    for k, c2 in enumerate(var):
        if c2 % 2 == 0:
            var2.append(c2)

l1 = []
sorteio(l1)
print(l1)

l2 = []
somapar(l1, l2)
print(l2)
