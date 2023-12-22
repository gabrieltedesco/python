def notas(*n, sit=False):
    dic = {}
    dic['total'] = len(n)
    dic['maior'] = max(n)
    dic['menor'] = min(n)
    m = 0
    for c in n:
        m += c
    dic['media'] = m/len(n)
    if sit:
        if dic['media'] > 7:
            dic['sit'] = 'BOA'
        elif 6 <= dic['media'] <= 7:
            dic['sit'] = 'RAZOAVEL'
        else:
            dic['sit'] = 'RUIM'
    return dic


r = notas(6, 8, 5, 10, 8, sit=True)
print(r)
