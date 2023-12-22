dic = {}
dic['nome'] = input('Nome: ')
dic['média'] = float(input('Média: '))
if dic['média'] >= 6:
    dic['sit'] = 'aprovado'
else:
    dic['sit'] = 'reprovado'
print(f'O aluno {dic["nome"]}, que tem média {dic["média"]}, está {dic["sit"]}!')
