n = input('Digite um expressão: ')
Pa = Pf = 0 #P. abertos e P. fechados
for c in n:
    if c == '(':
        Pa += 1
    if c == ')':
        Pf += 1
    if not Pa >= Pf:
        break
if Pa != Pf or Pf > Pa:
    print('Expressão inválida!')
else:
    print('Expressão válida!')
