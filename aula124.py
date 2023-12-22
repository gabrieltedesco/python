print("A sintaxe de herança múltipla em python é simples.")
class Calculadora:
    def calcula(self, expressão):
        self.valor = eval(expressão) #faz a validação de uma expressão

class Falador:
    def fala(self):
        print('Ei, meu valor é', self.valor) #faz o print de uma expressão

class CalculadoraFalante(Calculadora, Falador): #classe recebe duas superclasses
    pass

cf = CalculadoraFalante()
cf.calcula('1+2*3') #método e atributos por herança múltipla
cf.fala()


print("E se eu quiser usar um método da superclasse, ou seja, presente no construtor dela?")
print("Será que eu posso usar o super??")

class Primeira(object):
    def __init__(self):
        self.p1 = 1
        print("primeira")

class Segunda(object):
    def __init__(self):
        self.p2 = 2
        print("segunda")

class Terceira(Primeira, Segunda):
    def __init__(self):
        super(Terceira, self).__init__() #tenta usar o super para acessar o construtor de outras classes
        try: #porém o super procura o 'nome' do método e o n° de 'argumentos' necessários, retornando o primeiro método que achar
            print("Acabou!", self.p1, self.p2) #retorna somente o construtor da primeira, não de ambas → não existe self.p2
        except Exception as E:
            print(E)

t_1 = Terceira()


print("Corrigindo o erro do super() - formato recomendado")

class Primeira(object):
    def __init__(self):
        self.p1 = 1
        print("primeira")

class Segunda(object):
    def __init__(self):
        self.p2 = 2
        print("segunda")

class Terceira(Primeira, Segunda):
    def __init__(self):
        Primeira.__init__(self) #classe.__init__ com a subclasse como argumento, pois Terceira é um objeto de Primeira
        Segunda.__init__(self)
        print("Acabou!", self.p1, self.p2)

t_2 = Terceira()