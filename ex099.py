l = []
def maior(* n):
    c = max(l)
    print(f'O maior número é {c}')


while True:
    l.append(int(input('Valor: ')))
    r = input('Quer continuar? [S/N] ').upper()
    if r == 'N':
        break
print(l)
maior(l)
