ma = me = 0
for c in range(0, 5):
    n = int(input(f'Digite o peso da {c+1}° pessoa: '))
    if c == 0:
        ma = n
        me = n
    else:
        if n >= ma:
            ma = n
        if n <= me:
            me = n
print(f'O maior peso foi {ma}kg e o menor peso foi {me}kg')
