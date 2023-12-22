import shelve
#Data Base para organizar o Pickle
database = shelve.open('shelve.db') #modo de abertura 'create'
database['lista'] = [1, 2, 3]
class Pessoa:
    pass
Pedro = Pessoa()
database['nome1'] = Pedro
print(database['lista'])
print(database['nome1'])

for keys in database:
    print(keys, end=' ')

database.close()
