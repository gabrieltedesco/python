n = c = 0
while True:
    c = 1
    n = int(input('Digite um valor: '))
    if n < 0:
        break
    while c <= 10:
        print(f'{n} x {c:2} = {n*c}')
        c += 1
    print('='*16)
