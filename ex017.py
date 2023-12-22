from math import sqrt
print('Dado um triângulo retângulo,')
c1 = float(input('Valor de um cateto: '))
c2 = float(input('Valor do outro cateto: '))
h = sqrt(c1**2 + c2**2)
print(f'O valor da hipotenusa vale {h:.2f}')
