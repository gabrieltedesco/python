import json
#Javascript Object Notation Serializer
arquivo = open('teste.json', 'wb')

data = {'nome': 'Pedro', 'idade': 18, 'altura': 1.80}
data_string = json.dumps(data) #conversão do dict em uma string - print(type(data_string))
arquivo.write(data_string.encode())

data = [1, 2, 3]
data_string = json.dumps(data)
arquivo.write(data_string.encode())

data = ('a', 'b', 'c')
data_string = json.dumps(data)
arquivo.write(data_string.encode())
arquivo.close()

arquivo = open('teste.json', 'rb')
data_total = arquivo.readline()
print(data_total)

data_1 = data_total[:45].decode() #descodificando o dict
obj_1 = json.loads(data_1) #conversão da string novamente em dicionário
print(obj_1, type(obj_1))

#para armazenar classes, necessita-se da transformação em dicionário primeiro
class Pessoa:
    pass
dic = Pessoa().__dict__
data_obj = json.dumps(dic)
