tupla = ('Lápis', 1.50,
         'Borracha', 0.50,
         'Caneta', 2.00,
         'Caderno', 7.50,
         'Planner', 10.00)
c = 0
print('='*32)
print('{:^30}'.format('LISTA DE PREÇOS'))
print('='*32)
while True:
    print(f'{tupla[c]:.<25} {tupla[c+1]:.2f}')
    c += 2
    if c == len(tupla):
        break
