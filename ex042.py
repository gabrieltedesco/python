n1 = int(input('Primeiro segmento: '))
n2 = int(input('Segundo segmento: '))
n3 = int(input('Terceiro segmento: '))
if n2 + n3 > n1 and n1 + n3 > n2 and n1 + n2 > n3:
    print('Esse triângulo existe. ')
    if n1 == n2 == n3:
        print('Sua classificação é equilátero')
    elif n1 == n2 and n1 != n3 or n1 == n3 and n1 != n2 or n2 == n3 and n2 != n1:
        print('Sua classificação é isósceles')
    elif n1 != n2 != n3:
        print('Sua classificação é escaleno')
else:
    print('Esse triângulo não pode existir.')
