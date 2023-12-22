class Ponto:
    def __init__(self, x, y):
        self.abcissa = x
        self.ordenada = y

    def mostraPonto(self):
        print(f'As coordenadas do ponto ({self.abcissa},{self.ordenada})')

class Retangulo:
    def __init__(self, base, altura, ponto_1):
        self.base = base
        self.altura = altura
        self.Vertice = ponto_1

    def mostraCentro(self):
        abcissaCentro = self.Vertice.abcissa + self.base/2
        ordenadaCentro = self.Vertice.ordenada + self.altura/2
        return abcissaCentro, ordenadaCentro

ponto_1 = Ponto(1, 5)
ponto_1.mostraPonto()
retangulo_1 = Retangulo(6, 8, ponto_1)
print(f'O retângulo tem base {retangulo_1.base} e altura {retangulo_1.altura}')
retangulo_1.Centro = retangulo_1.mostraCentro()
print(f'Para o retângulo dado, seu centro é {retangulo_1.Centro}')
