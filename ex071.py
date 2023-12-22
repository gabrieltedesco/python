print('='*20)
print('{:^20}'.format('BANCO CV'))
print('='*20)
n = int(input('Quanto deseja sacar: R$'))
a = n // 50
b = (n - 50*a) // 20
c = (n - 50*a - 20*b) // 10
d = (n - 50*a - 20*b - 10*c)
if a != 0:
    print(f'Cédulas de R$50: {a}')
if b != 0:
    print(f'Cédulas de R$20: {b}')
if c != 0:
    print(f'Cédulas de R$10: {c}')
if d != 0:
    print(f'Cédulas de R$1: {d}')
