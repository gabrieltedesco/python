c = p = pr = t = 0
n = ''
ba = ''
bar = 0
r = 'S'
while True:
    n = input('Nome do produto: ')
    pr = int(input('Preço: R$ '))
    t += pr
    if pr >= 1000:
        p += 1
    if c == 0:
        bar = pr
        ba = n
    c += 1
    if pr < bar:
        ba = n
    r = input('Quer continuar?[S/N] ').upper()
    if r == 'N':
        break
    print('='*16)
print('='*25)
print(f'''Resultado
Total gasto: R${t}
Produtos que custam mais de R$1000: {p}
Produto mais barato: {ba}''')
