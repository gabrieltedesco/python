import struct
nome = 'Joao'
idade = 25
altura = 1.75

#string = bytes('palavra', 'utf-8')
#print(string)
#print(string[0])
# uso de I para int pequeno, Q para int grande, f para float pequeno, d para float grande, ? para booleano

codifica = struct.pack('4s I f', nome.encode(), idade, altura)
print(codifica) #arquivo codificado
arquivo = open('pessoa.cod', 'wb')
print(arquivo.write(codifica)) #numero de caracteres do arquivo
print(codifica.split(b'a')) #variáveis em bytes usam os métodos normais, mais adaptados ao formato b''
arquivo.close()

arquivo = open('pessoa.cod', 'rb')
codigo = arquivo.readline()
descodifica = struct.unpack('4s I f', codigo)
print(descodifica)
nome = descodifica[0].decode()
