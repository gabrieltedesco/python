tupla = ('aprender', 'programar', 'linguagem', 'python')
for c in range(0, len(tupla)):
    print(f'\nNa palavra {tupla[c]} temos as vogais: ', end='')
    for d in range(0, len(tupla[c])):
        if tupla[c][d] in 'aeiou':
            print(f'{tupla[c][d]} ', end='')
