n = int(input('Digite o preço do produto: R$'))
print('Escolha a opção de pagamento:')
print('''[1] À vista dinheiro/cheque
[2] À vista cartão
[3] Em até 2x no cartão
[4] 3x ou mais no cartão''')
op = int(input('Sua opção: '))
if op == 1:
    print(f'O preço será de R${0.9*n:.2f}')
elif op == 2:
    print(f'O preço será de R${0.95*n:.2f}')
elif op == 3:
    print(f'O preço será de R${n:.2f}')
elif op == 4:
    print(f'O preço será de R${1.2*n:.2f}')
