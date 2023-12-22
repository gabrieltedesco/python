#exercício 064
n = 0
c = 0
s = 0
while True:
    n = int(input('Digite um valor: '))
    if n == 999:
        break
    s += n
    c += 1
print(f'Foram digitados {c} valores e a soma deles vale {s}')
