s = 0
for c in range(1, 501):
    if c % 3 == 0 and c % 2 == 1:
        s += c
print(f'A soma dos ímpares múltiplos de 3 de 1 a 500 vale {s}')
