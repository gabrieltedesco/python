n = int(input('Digite o salário: R$'))
if n > 1250:
    print(f'O novo salário será de {1.10*n:.2f}')
else:
    print(f'O novo salário será de {1.15*n:.2f}')