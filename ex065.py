n = c = m = ma = me = 0
r = 'S'
while True:
    n = int(input('Digite um valor: '))
    m += n
    c += 1
    if c == 1:
        ma = me = n
    if n > ma:
        ma = n
    if n < me:
        me = n
    r = input('Quer continuar?[S/N] ').upper()
    if r == 'N':
        break
print(f'A média dos valores é {m/c:.2f}, o maior valor foi {ma} e o menor valor foi {me}')
