d = 0
n = int(input('Digite um valor: '))
for c in range(n, 0, -1):
    if n % c == 0:
        d += 1
if d == 2:
    print(f'O número {n} é primo')
else:
    print(f'O número {n} não é primo')
