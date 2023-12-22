def aumentar(p=0, t=0):
    p1 = p*(1+t/100)
    return p1


def dobro(p=0):
    p1 = p*2
    return p1


def diminuir(p=0, t=0, edt=False):
    p1 = p*(1-t/100)
    return p1 if not edt else fmt(p1)


def metade(p=0, edt=False):
    p1 = p/2
    return p1 if not edt else fmt(p1)


def fmt(p=0, edt=False):
    return f'R${p:.2f}'.replace('.', ',')


def resumo(p=0, aum=0, dim=0):
    print('='*30)
    print('RESUMO DO VALOR'.center(30))
    print('=' * 30)
    print(f'Preço pedido: \t{fmt(p)}')
    print(f'O dobro vale \t{dobro(p)}')
    print(f'A metade vale \t{metade(p, True)}')
    print(f'Mais {aum}% vale \t{aumentar(p, aum)}')
    print(f'Menos {dim}% vale \t{diminuir(p, dim, True)}')
    print('=' * 20)



#ex107 : comandos de manipulação do valor
#ex108 : comandos de formatação da exibição
#ex109 : criação de um parâmetro para a formatação
#ex110 : criação do comando resumo