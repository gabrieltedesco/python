n = int(input('Qual a velocidade do carro em Km/h? '))
if n<= 80:
    print('Sua velcidade está na faixa permitida! Boa viagem.')
else:
    print(f'Velocidade acima da permitida! Você foi multado em R${(n - 80)*7:.2f}')
