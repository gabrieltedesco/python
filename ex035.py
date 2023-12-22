n1 = float(input('Digite o primeiro segmento: '))
n2 = float(input('Digite o segundo segmento: '))
n3 = float(input('Digite o terceiro segmento: '))
if n2 + n3 > n1 and n1 + n3 > n2 and n1 + n2 > n3:
    print('Os segmentos podem formar um triângulo')
else:
    print('Os segmentos não podem formar um triângulo')
