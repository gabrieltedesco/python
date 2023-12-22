class Quadrado:
    def __init__(self, ladoMetro):
        self.lado = ladoMetro
        print(f'Método construtor acionado! Novo quadrado com {ladoMetro}m de lado')


    def mudarLado(self):
        novoLado = int(input('Digite o novo valor: '))
        self.lado = novoLado
        print(f'Valor do lado alterado para {novoLado}m')


    def valorLado(self):
        valorLado = quadrado_1.lado
        print(f'O valor do lado do quadrado vale {valorLado}m')


    def calcularArea(self):
        valorArea = quadrado_1.lado * quadrado_1.lado
        print(f'O valor da área do quadrado vale {valorArea}m²')


quadrado_1 = Quadrado(5)
quadrado_1.mudarLado()
quadrado_1.valorLado()
quadrado_1.calcularArea()
