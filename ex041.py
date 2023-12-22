n = int(input('Ano de nascimento: '))
d = 2021 - n
if d <= 9:
    print('Sua classificação é Mirim')
elif 9 < d <= 14:
    print('Sua classificação é Infantil')
elif 14 < d <= 19:
    print('Sua classificação é Junior')
elif 19 < d <= 25:
    print('Sua classificação é Sênior')
elif d > 25:
    print('Sua classificação é Master')
