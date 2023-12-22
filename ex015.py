print('No aluguel do carro, ')
d = float(input('Dias alugados: '))
km = float(input('Km percorridos: '))
print(f'O preço a ser pago pelo aluguel é R${d*60 + km*0.15:.2f}')
