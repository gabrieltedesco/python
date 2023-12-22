#Decoradores de Funções
print("Algumas funções construídas precisam ser customizadas")

def p_decorador(func):
    def nova_func(num1, num2):
        return "<p>" + func(num1, num2) + "</p>"
    return nova_func

def div_decorador(func):
    def nova_func(num1, num2):
        return "<div>" + func(num1, num2) + "</div>"
    return nova_func

def strong_decorador(func):
    def nova_func(num1, num2):
        return "<strong>" + func(num1, num2) + "</strong>"
    return nova_func

@p_decorador
@div_decorador
@strong_decorador
def devolve_trecho(num1, num2):
    return f'Resultado: {num1 * num2}'

print(devolve_trecho(2, 3)) #retorna <p><div><strong> </strong></div></p>


print("Note que as funções decoradoras tem estruturas")
print("bastantes semelhantes, então o ideal seria")
print("escrever uma única função tag_decorador")
print("que recebece um argumento de forma a colocar a tag adequada")

def tags(nome_tag): #uso de 3 funções, a que passa novos parâmetros, a decoradora e a função que modifica os dados
    def tags_decorador(func):
        def nova_func(num1, num2):
            return "<" + nome_tag + ">" + func(num1, num2) + "</" + nome_tag + ">"
        return nova_func
    return tags_decorador

@tags('p')
def devolve_trecho(num1, num2):
    return f'Resultado: {num1 * num2}'

print(devolve_trecho(2,3)) ##retorna <p><div><strong> </strong></div></p>


****
#Decoradores de Métodos
print("Decoradores de métodos funcionam assim como")
print("decoradores de funções usando a sintaxe do @")
print("Alguns decoradores de método populares apresentaremos")
print("São eles @staticmethod, @classmethod e @property")

print("@staticmethod indica que o dado método é estatico")
print("logo deverá ser chamado usando a classe e não uma")
print("instância da classe, assim a instância não")
print("deve ser passada como argumento. Por exemplo: ")

class A(object):
    @staticmethod
    def method(*argv):
        return argv

a = A()
print("Com o @staticmethod: ", a.method([1, 2, 3, 4])) #([1, 2, 3, 4],)
                                                       #indica que não precisa da instância sendo passada como argumento do método
class A(object):
    def method(*argv):
        return argv

a = A()
print("Sem o @staticmethod: ", a.method([1, 2, 3, 4])) #(<__main__.A object at 0x000001F247C09A50>, [1, 2, 3, 4])


print("@classmethod, ao inves da instância ser passada")
print("como argumento para o método, a classe será passada")

class A(object):
    @classmethod
    def method(*argv):
        return argv

a = A()
print("Sem o @classmethod: ",a.method([1, 2, 3, 4])) #(<class '__main__.A'>, [1, 2, 3, 4]), repassa a instância da classe A
                                                     #recebe a classe como argumento


print("Um decorador importante refere-se as propriedades")
print("Veja no exemplo que por meio dos decoradores substituimos")
print("A linha de criação da propriedade e ainda todos os métodos")
print("possuem os mesmos nomes")

class Pessoa:
    def __init__(self, prim_nome, ult_nome):
        self.prim_nome = prim_nome
        self.ult_nome = ult_nome

    @property #substitui o método que faz um descritor por meio de criação de funções
    def nome(self): #contém a função getter imbutida nele para o atributo 'nome'
        return self.ult_nome, self.prim_nome

    @nome.setter
    def nome(self, valor):
        self.prim_nome = valor

    @nome.deleter
    def nome(self):
        del self.prim_nome
        del self.ult_nome


p = Pessoa('Luis', 'Rodrigo')
print(p.nome)
p.nome = 'Alchin, Martin'
print(p.nome)
del p.nome


****
#Decoradores de Classes
print("Podemos criar decoradores de classes, isto é")
print("decoradores que irão mudar todo o funcionamento de uma dada classe")

print("No exemplo abaixo vemos o decorador 'singleton' que")
print("faz com que apenas uma instância de classe possa ser criada")

instancias = {}
def singleton(umaClasse):
    def onCall(*args, **kwargs):
        print("onCall foi chamado agora!!")
        if umaClasse not in instancias: #verifica se a classe já uma chave do dict instancias
            instancias[umaClasse] = umaClasse(*args, **kwargs)
        return instancias[umaClasse]
    return onCall

@singleton #função decoradora da classe Pessoa que permite somente uma única instância
class Pessoa:
    def __init__(self, nome, horas, ganho):
        self.nome = nome
        self.horas = horas
        self.ganho = ganho

    def paga(self):
        return self.horas * self.ganho


bob = Pessoa('Bob', 40, 10) #retorna "onCall foi chamado agora!!"
print(bob.nome, bob.paga()) #retorna Bob 400
sue = Pessoa('Sue', 50, 20) #retorna "onCall foi chamado agora!!"
print(sue.nome, sue.paga()) #retorna Bob 400


print("Uma 'classe decoradora' por outro lado")
print("consiste numa classe que irá decorar a outra")
print("logo a classe decoradora deverá receber uma classe como argumento")

print("Por exemplo, suponhamos que se queira acompanhar os métodos")
print("usados por uma determinada classe. Iremos criar uma classe")
print("decoradora Trace que permitira acompanhar a execução de")
print("uma classe decorada por ela")

class Tracer:
    def __init__(self, umaClasse): #método construtor da classe Tracer
        print("Construtor foi chamado!!")
        self.umaClasse = umaClasse

    def __call__(self, *args): #método que obtém todos os atributos da classe decorada
        print("Chamamos o método __call__")
        self.wrapped = self.umaClasse(*args) #seld.wrapped é a instância da classe Tracer que foi criada com a classe Spam
                                             #é objeto de Tracer que vai decorar o objeto recido de Spam
        return self

    def __getattr__(self, atrnome): #método que é chamado quando atributos ou método da classe Spam são chamados
        print('Trace: ' + atrnome)  #como o método display não existe em Tracer, o getattr é chamado e adiciona o método display na instancia self.wrapped
        return getattr(self.wrapped, atrnome) #ao retornar, então que é chamado 'display' de Spam, pois o Tracer teria que verificar se essa função sofreria alguma decoração
                                              #esse getattr(self.wrapped, atrnome) permite a modificação do método pela mudança de 'atrnome' pela chamada de uma função interna 'display_change', por exemplo
    def display_change(self, func):
        return f'<p>{func}</p>'

@Tracer  #Chama o construtor de Tracer por "Construtor foi chamado!!"
class Spam: #é como uma classe 'filha' de Tracer
    def display(self):
        print('Spam!' * 8)

print("Vamos começar o teste...")
s = Spam()  #Chama o Call de Tracer por "Chamamos o método __call__"
s.display() #retorna 'Trace: display' por causa do getattr e 'Spam!' * 8

#s é uma instância do Tracer, não do Spam
