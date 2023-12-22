m = 0
for c in range (0, 7):
    n = int(input('Ano de nascimento: '))
    d = 2021 - n
    if d >= 18:
        m += 1
print(f'Ao total temos {m} pessoas maiores de idade')
