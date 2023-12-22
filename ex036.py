n = float(input('Valor da casa: '))
s = float(input('Seu salário: '))
t = int(input('Anos de pagamento: '))
p = n/(12*t)
if 0.3*s <= p:
    print(f'Seu empréstimo foi negado pois a prestação seria de R${p:.2f}')
elif 0.3*s > p:
    print(f'Seu empréstimo foi aprovado pois a prestação custará R${p:.2f}')
