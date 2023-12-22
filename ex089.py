l = []
g = []
h = []
while True:
    n = input('Nome: ')
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    h.append(n1)
    h.append(n2)
    g.append(n)
    g.append(h[:])
    l.append(g[:])
    g.clear()
    h.clear()
    r = input('Quer continuar?[S/N] ').upper()
    if r == 'N':
        break
print(f'{"No":4}{"NOME":10}{"Media":>5}')
print('='*20)
for c in range(0, len(l)):
    print(f'{c:<4}{l[c][0]:10}{(l[c][1][0] + l[c][1][1])/2:>5}')
while True:
    r = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    if r == 999:
        break
    print(f'As notas de {l[r][0]} são {l[r][1]}')
