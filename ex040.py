n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2)/2
if m < 5.0:
    print(f'Você foi reprovado com média {m:.1f}')
elif 5.0 <= m < 7:
    print(f'Você está de recuperação com média {m:.1f}')
elif m >= 7:
    print(f'Você foi aprovado com média {m:.1f}')
