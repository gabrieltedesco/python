print("Propriedades e Descritores")

print("Propriedades - Permitem gerenciar a criação e manipulação de atributos de uma da classe")
print("Semelhante aos métodos __getattr__, __setattr")
print("e __getattribute__ porem menos genéricos, ou seja, atributos únicos e já previamente definidos")

class Pessoa(object):
    def __init__(self, nome):
        self._nome = nome # 1 underline = propriedade, 2 underline = atributo privado
    def getNome(self):
        print('Obtendo...')
        return self._nome
    def setNome(self, valor):
        print('Modificando...')
        self._nome = valor
    def delNome(self):
        print('Removendo...')
        del self._nome
    nome = property(getNome, setNome, delNome, "Documentação da propriedade nome")
                    #função property recebe 3 métodos e uma string
                    #os valores pré-definidos dos métodos é None

bob = Pessoa('Bob Smith')
print(bob.nome) #retorna 'Obtendo..,' + 'Bob Smith'
bob.nome = 'Robert Smith' #retorna 'Modificando..,'
print(bob.nome) #retorna 'Obtendo..,' + 'Robert Smith'
print(Pessoa.nome.__doc__)


****
print("Descritores - Funcionam como propriedades")
print("entretanto os métodos get, set, del e a descrição")
print("são todos feitos por uma classe específica com protocolo bem definido")

class Nome(object): #objeto descritor gerado por Pessoa()
    "Documentação da propriedade nome"
    def __get__(self, instancia, dono):
        print('Obtendo...')
        return instancia._nome
    def __set__(self, instancia, valor):
        print('Modificando...')
        instancia._nome = valor
    def __delete__(self, instancia):
        print('Removendo...')
        del instancia._nome

class Pessoa(object):
    def __init__(self, nome):
        self._nome = nome
    nome = Nome()

bob = Pessoa('Bob Smith')
nome = Nome()
print(bob.nome)
bob.nome = 'Robert Smith'
del bob.nome
print(Nome.__doc__)

print("A função 'property' em python é usada para criar um descritor, ou seja, o objeto descritor")
print("Os métodos definidos dentro de property são: init, get, set, delete, getattribute, new")
print("Assim, type(property) retorna class type, ou seja, uma metaclasse que gera classes de descritores")