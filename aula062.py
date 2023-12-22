class ObjetoGrafico(object):
    def __init__(self, cor1, cor2, sitInterna=False):
        self.corInterna = cor1
        self.corExterna = cor2
        self.preenchimento = sitInterna

class Retangulo(ObjetoGrafico):
    def __init__(self, base, altura, cor1, cor2, sitInterna=False):
        super(Retangulo, self).__init__(cor1, cor2, sitInterna=False)
        self.base = base
        self.altura = altura
    def calculaArea(self):
        print(f'A área do retângulo vale {self.base*self.altura}')

class Circulo(ObjetoGrafico):
    def __init__(self, raio, cor1, cor2, sitInterna=False):
        super(Circulo, self).__init__(cor1, cor2, sitInterna=False)
        self.raio = raio
    def calculaArea(self):
        print(f'A área do círculo vale {(self.raio**2)}π')

circulo1 = Circulo(5, 100, 200, False)
circulo1.calculaArea()
retangulo1 = Retangulo(4, 6, 100, 200, False)
retangulo1.calculaArea()
