a = input('Digite algo: ')
print(f'O tipo primitivo é {type(a)}')
print(f'Só tem espaços? {a.isspace()}')
print(f'É um número? {a.isnumeric()}')
print(f'É alfanumérico? {a.isalnum()}')
print(f'Está em minúsculas? {a.islower()}')
