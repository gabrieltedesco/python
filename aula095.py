import random
from tkinter import *
from rascunhos import *

class Jogo(object):
    def __init__(self):
        #Criando a tela principal do jogo
        self.root = Tk()
        self.root.geometry(f'{largura}x{altura}')
        self.root.resizable(False, False)
        self.root.title('Jogo da Bola')
        #Criando uma frame para conter o canvas
        self.frame = Frame(self.root, bg='black')
        self.frame.pack()
        #Criando a tela do Canvas
        self.canvas = Canvas(self.frame, bg='black', width=canvas_l, height=canvas_a, cursor='')
        self.canvas.pack()
        #Criando um botão
        self.startBot = Button(self.root, text='START', command=self.Jogar)
        self.startBot.pack()
        self.novoJogo()

        self.root.mainloop()

    def novoJogo(self):
        #Criando os elementos de um novo jogo
        self.player = self.canvas.create_rectangle((canvas_l//2, 350), (canvas_l//2 + 100, 370), fill='green', tags='player')

        #Criando os retângulos
        self.retangulos = []
        linhas, colunas, espaco = 5, 8, 2
        base, altura, posicao_0 = 48, 20, 50
        for i in range(linhas):
            cor = random.choice(['green', 'orange', 'blue', 'red', 'white', 'yellow', 'purple', 'lightgreen'])
            for j in range(colunas):
                r = self.canvas.create_rectangle((base*j + espaco*(j+1), altura*i + espaco*(i+1) + posicao_0),
                                             (base*j + espaco*(j+1) + base, altura*i + espaco*(i+1) + posicao_0 + altura),
                                             fill=cor)
                self.retangulos.append(r)

        #Criando a bola
        raio = 30
        pbola = (100, 200)
        self.bola = self.canvas.create_oval((pbola[0], pbola[1]), (pbola[0]+raio, pbola[1]+raio),
                                            fill='red', outline='white', tags='bola')
        self.bola_vx = self.bola_vy = 10
        self.bola_x, self.bola_y = pbola

    def Jogar(self):
        if True:
            self.Update()
            self.root.after(10, self.Jogar)

    def Update(self):
        #Redefinir as condições do jogo
        self.canvas.itemconfig(self.player, fill='blue')
        self.canvas.move('bola', self.bola_vx, self.bola_vy)
        self.bola_x += self.bola_vx
        self.bola_y += self.bola_vy

        if self.bola_x > canvas_l-30 or self.bola_x < 0:
            self.bola_vx *= -1
        if self.bola_y > canvas_a-30 or self.bola_y < 0:
            self.bola_vy *= -1

        self.verificaColisao()

    def verificaColisao(self):
        #Criando uma bounding box para a bola
        pbola2 = self.canvas.bbox('bola')
        #Armazenando o id dos objetos que colidem com a bola
        colisao = self.canvas.find_overlapping(*pbola2)
        if len(colisao) != 0 and colisao[0] != self.player:
        #self.player não é um objeto, é um valor de id
        #objeto mais próximo do canto superior esquerdo da bola
            maisprox = self.canvas.find_closest(pbola2[0], pbola2[1])
            for i in self.retangulos:
                if i == maisprox[0]:
                    self.retangulos.remove(i)
                    self.canvas.delete(i)
                    self.bola_vy *= -1
                    return

Jogo()