class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        print(f'Método construtor acionado! Novo retângulo criado')


    def mudarLado(self):
        novaBase = int(input('Valor da nova base: '))
        novaAltura = int(input('Valor da nova altura: '))
        self.base = novaBase
        self.altura = novaAltura

    def valorLado(self):
        print(f'O valor da base do retângulo é {self.base}m e da altura é {self.altura}m')


    def calcularArea(self):
        print(f'O valor da área do retângulo vale {self.base * self.altura}m²')


    def calcularPeri(self):
        print(f'O perímetro do retângulo vale {2*self.base + 2*self.altura}m')


basePiso = int(input('Valor da base: '))
alturaPiso = int(input('Valor da altura: '))
retangulo_1 = Retangulo(basePiso, alturaPiso)
retangulo_1.valorLado()
retangulo_1.calcularArea()
retangulo_1.calcularPeri()

