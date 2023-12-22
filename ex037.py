n = int(input('Digite um inteiro: '))
print('[1] Converter para binário')
print('[2] Converter para octal')
print('[3] Converter para hexadecimal')
p = int(input('Sua opção: '))
if p == 1:
    print(f'{n} em binário vale {bin(n)[2:]}')
elif p == 2:
    print(f'{n} em hexadecimal vale {oct(n)[2:]}')
elif p == 3:
    print(f'{n} em octal vale {hex(n)[2:]}')
