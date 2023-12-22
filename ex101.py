def voto(ano):
    i = 2023 - ano
    if i < 18:
        return f'Com {i} anos: Não vota!'
    elif 18 <= i <= 60:
        return f'Com {i} anos: Voto obrigatório!'
    elif i > 60:
        return f'Com {i} anos: Voto opcional!'


n = voto(int(input('Em que ano você nasceu: ')))
print(n)
