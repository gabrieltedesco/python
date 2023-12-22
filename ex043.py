m = float(input('Massa (kg): '))
h = float(input('Altura (m): '))
IMC = m/h**2
if IMC < 18.5:
    print(f'Seu IMC vale {IMC:.2f} e sua classificação é Abaixo do peso')
elif 18.5 <= IMC < 25:
    print(f'Seu IMC vale {IMC:.2f} e sua classificação é Peso ideal')
elif 25 <= IMC < 30:
    print(f'Seu IMC vale {IMC:.2f} e sua classificação é Sobrepeso')
elif 30 <= IMC < 40:
    print(f'Seu IMC vale {IMC:.2f} e sua classificação é Obesidade')
elif IMC >= 40:
    print(f'Seu IMC vale {IMC:.2f} e sua classificação é Obesidade')
