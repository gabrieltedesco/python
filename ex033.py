n1 = int(input('Digite o primeiro valor: '))
ma = n1
me = n1
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))
if n2 > n3 and n2 > ma:
    ma = n2
if n3 > n2 and n3 > ma:
    ma = n3
if n2 < n3 and n2 < me:
    me = n2
if n3 < n2 and n3 < me:
    me = n3
print(f'O menor valor foi {me} e o maior valor foi {ma}')
