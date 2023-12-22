print("Para construir objetos indexáveis precisamos construir alguns")
print("alguns métodos específicos dentro do nosso objeto: __getitem__, __setitem__, __len__, __delitem__")

****
print("__getitem__ --> Permite pegar o objeto contido no indice")
class MinhaLista(object):
    def __getitem__(self, index):
        return index ** 2

a = MinhaLista()
for i in range(5):
    print(a[i])
#Ou seja, ao chamar o index de algum objeto criado, nesse caso o "a", ele chama o método getitem e retorna o index^2

print("O que acontece se eu tentar percorrer esse objeto com um for loop?")
for i in a:
    print(i)
print("Veja que a lista não tem um limite por isso o for loop é infinito. Poderíamos corrigir isso fazendo:")


class MinhaLista(object):
    def __init__(self, tamanho):
        self.len = tamanho #define um tamanho limitado para o objeto

    def __getitem__(self, index):
        if index < self.len:
            return index ** 2
        else:
            raise StopIteration

a = MinhaLista(5)
for i in a:
    print(i)

#OU TAMBÉM

class MinhaLista(object):
    def __init__(self, *args):
        self.data = [] #define já os elementos possíveis do objeto
        for arg in args:
            self.data.append(arg)

    def __getitem__(self, index):
        return self.data[index] ** 2

a = MinhaLista(0, 1, 2, 3, 4)
for i in a:
    print(i)

print("É possível usar slices neles a partir desse método")
class MinhaLista:
    def __getitem__(self, index):
        if isinstance(index, int): #isistance verifica se um objeto faz parte de um determinada classe → a[1]
            print('indexing', index) #indexing 1
        else: #a[1:3], pois "1:3" não é um inteiro
            print('slicing', index.start, index.stop, index.step) #slicing 1 3 None


****
print("Assim como podemos obter o valor de uma determinada posição")
print("para colocar um valor numa dada posição é preciso um método")
print("especial, no caso o método __setitem__")

class SequenciaAritimetica:
    def __init__(self, start=0, step=1):
        self.start = start
        self.step = step
        self.modificado = {}

    def __getitem__(self, index):
        if isinstance(index, int):
            if index < 0: raise IndexError #em Listas o índice poderia ser maior que zero
            try:
                return self.modificado[index] #tenta retornar o valor contido na 'chave index' do dict "modificado"
            except KeyError:
                return self.start + index * self.step #retorna o novo elemento da sequência aritmética a + nr
        else: #fazendo o slicing
            if index.step == None: step = 1
            else: step = index.step
            data = [] #lista com os valores pedidos no slicing
            for i in range(index.start, index.stop, step): #percorrendo os elementos dentro do slicing
                data.append(self[i])
            return data

    def __setitem__(self, index, value): #s[3] = 4 para alterar o valor do objeto
        if index < 0: raise IndexError
        self.modificado[index] = value

s = SequenciaAritimetica(2, 3)
#[5, 8, 11, 15] se torna [5, 8, 4, 15]


****
print("Para deletar uma chave é preciso utilizar o método")
print("__delitem__")

class SequenciaAritimetica:
    def __init__(self, start=0, end=1, step=1):
        self.start = start
        self.step = step
        self.end = end
        self.data = list(range(start, end, step)) #determinação efetiva dos valores de uma sequência ao ser chamada

    def __getitem__(self, index):
        if isinstance(index, int):
            if index < 0: raise IndexError
            try: return self.data[index]
            except KeyError: return self.data[index]
        else:
            return self.data[index] #DEVERIA fazer o slicing, não retorna o valor na chave index da 'data'

    def __setitem__(self, index, value):
        if index < 0: raise IndexError
        self.data[index] = value #alteração de algum valor

    def __delitem__(self, index):
        del self.data[index] #deleção de algum valor por del s[1]


****
print("Por fim para obter o tamanho de um objeto temos de colocar")
print("o método especial __len__")
print("E se um elemento está contido dentro do objeto")
print("utilizando o método __contains__")

class SequenciaAritmetica:
    def __init__(self, start=0, end=1, step=1):
        self.start = start
        self.step = step
        self.end = end
        self.data = list(range(start, end, step))
        self.len = len(self.data)

    def __getitem__(self, index):
        if isinstance(index, int):
            if index < 0: raise IndexError
            try:
                return self.data[index]
            except KeyError:
                return self.data[index]
        else:
            return self.data[index]

    def __setitem__(self, index, value):
        if index < 0: raise IndexError
        self.data[index] = value

    def __delitem__(self, index):
        del self.data[index]

    def __len__(self):
        return self.len

    def __contains__(self, value): #chama o método contains por meio do "in" que retorna um booleano
        return value in self.data #print(2 in s)


****
"Uso de getattr para acessar um atributo que não existe e setattr "
"para dar um valor para um atributo que não existe")

class Vazio:
    def __getattr__(self, atr_nome):
        if atr_nome == 'idade': #caso o atributo pedido seja a "idade", retorna um valor, mas não adiciona ao objeto
            return 40           #presentes em objetos que não permitem setar novos atributos
        else:
            raise AttributeError(atr_nome)

e = Vazio()
print(e.idade)

class ControleAcesso:
    def __setattr__(self, atr, valor): #presentes em objetos que não permitem setar novos atributos
        if atr == 'idade':
            self.__dict__[atr] = valor + 10 #retorna o valor 50
        elif atr == 'nome':
            self.__dict__[atr] = valor
        else:
            raise AttributeError(atr + ' não permitido')

c = ControleAcesso()
c.idade = 40
#o método getattribute() lida com atributos que já existem no objeto


****
print("2 - setitem, getitem --> Para dicionários")

class Vazio:
    def __getitem__(self, atr_nome): #passa uma string de nome do atributo ao invés de um índice como nos objetos
        if atr_nome == 'idade':      #pode ser passado uma string, um inteiro, uma tupla, uma lista ou até objetos como valores de chaves
            return 40
        else:
            raise AttributeError(atr_nome)

e = Vazio()
print(e['idade'])

class ControleAcesso:
    def __setitem__(self, atr, valor):
        if atr == 'idade':
            self.__dict__[atr] = valor + 10 #o novo atributo do dicionário terá o valor 50 adicionado
        else:
            raise AttributeError(atr + ' não permitido')


c = ControleAcesso()
c['idade'] = 40
print("Utilidade: Criação dos próprios dicionários")

print('3 - Objetos Chamáveis --> Funções')

class Op_Basicas:
    def __call__(self, qualquer_coisa): #protocolo call permite a chamada de funções de objetos
        return qualquer_coisa

o = Op_Basicas()
valor = o("Sou uma instância chamável")
print(valor)

input()

print("Utilidade principal: Tkinter")
print("Podemos definir como command para uma dada widget do")
print("tkinter como sendo um objeto chamável, assim poderíamos")
print("com facilidade manipular os atributos do objeto além de")
print("utilizar outros métodos de forma a obter mair controle sobre o aplicativo")


****
print("Metaclasses")
print("TUDO EM PYTHON É OBJETO")
print("essa frase se extende até mesmo para classes")
print("classes são objetos de uma classe")

print("type usando 3 argumentos")
print("Podemos usar a função type com 3 argumentos para")
print("construir novas classes. Por exemplo")

def criaClasse(**argumentos):
    return type("MinhaClasse", (object, ), argumentos) #retorna não um objeto, mas uma nova classe por ser uma metaclasse

a = criaClasse(idade = 13, olhos = 2) #"a" se torna uma instância de "Minha Classe", ou seja, uma classe
print(a)                               #classes são criadas de uma maneira mais dinâmica
print(a.idade, a.olhos)

print("Veja que criamos a classe MinhaClasse equivalente a")
class MinhaClasse(object):
    idade = 13
    olhos = 2


print("Se uma classe é um objeto de outra classe, que classe é essa?")
print("vamos usar o atributo __class__ para determinar isso")
class UmaClasse: pass
a = UmaClasse()
print(a.__class__) #retorna "UmaClasse" sendo "a" seu objeto
print(UmaClasse.__class__) #retorna "type", ou seja, type é uma metaclasse → a classe de outras classes

print("Type é conhecido por uma Metaclasse. Uma classe devolve um novo objeto")
print("enquanto que uma metaclasse devolve uma nova classe")
print("Type é a metaclasse padrão para as classes criadas")

print("Então como funciona a definição de uma classe em python?")
print("1 - Python ve a definição da classe")
print("2 - Python armazena a definição de métodos e atributos em um dicionário")
print("3 - Python chama Meta(nome_da_classe, pais_da_classe, dicionario) para determinar a Metaclasse da classe")
print("4 - Ao determinar a metaclasse ela é chamada para construir a classe")

print("Como definir minha própria metaclasse?")
print("Utilizar métodos __new__ e __init__")
class MinhaMeta(type):
    def __new__(meta, name, bases, dct):
        print('-----------------------------------')
        print("Alocando memória para a classe", name) #exibe "Alocando memória para a classe Minhaclasse"
        print(meta) #exibe a metaclasse da classe sendo definida, no caso "MinhaMeta"
        print(bases) #exibe a superclasse da classe sendo definida, no caso "object"
        print(dct) #atributos e métodos
        return super(MinhaMeta, meta).__new__(meta, name, bases, dct) # retorna, ao chamar o método new da superclasse da "MinhaMeta"
                                                                    # e passando meta como argumento, uma nova metaclasse

    def __init__(cls, name, bases, dct): #método construtor da MinhaMeta, ou seja, gerador de classes
        print('-----------------------------------')
        print("Inicializando classe", name)
        print(cls) #exibe a classe do objeto "MinhaClasse", ou seja, MinhaMeta
        print(bases) #exibe a superclasse da classe sendo definida, no caso "object"
        print(dct)
        super(MinhaMeta, cls).__init__(name, bases, dct)

class MinhaClasse(object, metaclass = MinhaMeta):
    #__metaclass__ = MinhaMeta
    def teste(self, param):
        pass
    atributo = 2

a = MinhaClasse()


print("É útil contruir um método __call__ no lugar do par __init__ e __new__")
print("para definir uma metaclasse")

class MinhaMeta(type):
    def __call__(cls, *args, **kwds): #cria um metaclasse que é chamável #args em tupla e kwds em dicionário
        print('__call__ de ', str(cls)) #retorna a classe "MinhaClasse"
        print('__call__ *args=', str(args)) #args(1, 2)
        return type.__call__(cls, *args, **kwds) #retorna a metaclasse a partir do type e sua chamada __call__

class MinhaClasse(object, metaclass = MinhaMeta):
    #__metaclass__ = MinhaMeta
    def __init__(self, a, b):
        print(f'MinhaClasse objeto com a={a} b={b}')

a = MinhaClasse(1, 2) #esses valores são repassado para o construtor da metaclasse que retorna a instância de MinhaMeta e chama o método call
                        #assim o método init da classe é chamado e a classe é criada


print("Veja exemplos de uso em controles de construção de classes")
print("http://eli.thegreenplace.net/2011/08/14/python-metaclasses-by-example")
