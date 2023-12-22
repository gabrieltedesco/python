a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
c = 0
while c < 10:
    print(a1, end=' ')
    a1 += r
    c += 1

d = 1
while d != 0:
    d = int(input('\nQuantos termos quer adicionar: '))
    for e in range(1, d+1):
        print(a1, end=' ')
        a1 += r
print('Progressão aritmética finalizada!')
