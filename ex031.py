n = int(input('Qual a distância a ser percorrida: '))
if n <= 200:
    print(f'O preço da passagem para {n}km vale R${0.5*n:.2f}')
else:
    print(f'O preço da passagem para {n}km vale R${0.45*n:.2f}')
