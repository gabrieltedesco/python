n = input('Digite uma frase: ').strip().lower()
c = n.count('a')
r = n.find('a')
print(f'Na frase há {c} letras A e a primeira na posição {r+1}')
