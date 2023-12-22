n = int(input('Quantos termos de Fibonacci quer: '))
a1 = 0
a2 = 1
t = 2
print(a1, a2, end=' ')
while t is not n:
    a3 = a1 + a2
    print(a3, end=' ')
    a1 = a2
    a2 = a3
    t += 1


