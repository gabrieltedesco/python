import dbm
#Data Base Manager
database = dbm.open('arquivo.db', 'c') #modo de abertura 'create' ou 'read'
database['email'] = 'pedro@gmail.com' #somente armazena strings, apesar de ser muito parecido com dict
database['idade'] = '24'
print(database['email'].decode(), int(database['idade']))
print(database.keys()) #keys também estão em formato de bytes

for keys in database:
    print(keys.decode(), end=' ')

database.close()
