from random import randint
c = randint(1, 10)
p = 0
n = 0
while p != c:
    p = int(input('Qual é seu palpite: '))
    n += 1
print(f'Foram necessárias {n} tentativas para acertar o número {c}')
