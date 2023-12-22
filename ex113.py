try:
    a = int(input('Digite o numerador: '))
    b = int(input('Digite o denominador: '))
    r = a / b
except Exception as erro:
    print(f'Infelizmente existe um erro de {erro.__class__}')
else:
    print(f'O resultado é {r}')
