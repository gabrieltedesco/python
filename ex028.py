from random import randint
n = int(input('Advinhe o número que pensei de 0 a 5: '))
c = randint(0, 5)
if n == c:
    print('Você acertou!')
else:
    print('Você errou!')

