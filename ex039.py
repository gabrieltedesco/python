n = int(input('Ano de nascimento: '))
d = 2021 - n
if d == 18:
    print('Está na hora de você se alistar!')
elif 18 > d > 0:
    print('Ainda não é hora de se alistar')
elif d > 18:
    print('Já passou da hora de se alistar')
