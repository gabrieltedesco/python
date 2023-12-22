from tkinter import *
from functools import partial
from math import floor

class Calculadora(object):
    def __init__(self, instancia):
        self.font1 = ('Verdana', '13', 'bold')
        self.font2 = ('Verdana', '10', 'bold')

        self.frame1 = Frame(instancia)  # checkbuttons
        self.frame2 = Frame(instancia)  # wrBot
        self.frame3 = Frame(instancia)  # ckBot
        self.frame4 = Frame(instancia)  # reBot
        self.frame5 = Frame(instancia)  # formulas
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.frame5.pack()

        self.bino = False
        self.binomial = Checkbutton(self.frame1, text='Modo binomial', bg='#B17C5D', fg='black',
                               font=self.font2, width=15, command=self.AtivacaoBino)
        self.binomial.pack(side=LEFT)
        self.poi = False
        self.poisson = Checkbutton(self.frame1, text='Modo poisson', bg='#B17C5D', fg='black',
                              font=self.font2, width=15, command=self.AtivacaoPoi)
        self.poisson.pack(side=LEFT)

        self.wrBot = Entry(self.frame2, width=30)
        self.wrBot.pack()

        self.ckBot = Button(self.frame3, text='Calcule', bg='#B17C5D', fg='#F2ECE9',
                            command=self.Calcular, font=self.font1)
        self.ckBot.pack()

        self.reBot = Label(self.frame4, text='Resultado', bg='#E1C2B0', fg='#58788C', pady=20, font=self.font2)
        self.reBot.pack()

        funcoes = ('media()', 'moda()', 'mediana()', 'soma(n, p, maior, menor = 0)',
                   'Comb(n, k)', 'desvio','Binomial(n, x, p)', 'poisson(l, x, t)', 'variancia', 'p(x > k)', 'p(x >= k)', 'p(x < k)',
                   'p(x <= k)', 'p(k1 < x < k2)', 'p(k1 <= x < k2)', 'p(k1 < x <= k2)', 'p(k1 <= x <= k2)')
        for i in range(len(funcoes)):
            if i%3==0:
                self.subframe1 = Frame(self.frame5)
                self.subframe1.pack() #side=TOP
            opBot = Button(self.subframe1, text=funcoes[i], bg='#B7896F', fg='#F2ECE9', width=25,
                           font=self.font2, pady=5, command=partial(self.Funcao, funcoes[i]))
            opBot.pack(side=LEFT)

        self.delete = Button(self.subframe1, text='del', bg='#B7896F', fg='white', width=25,
                             font=self.font2, pady=5)
        self.delete.pack(side=LEFT)

    def Calcular(self):
        self.reBot['text'] = self.IdentificaFuncao()
        self.wrBot.delete(0, END)

    def IdentificaFuncao(self):
        texto = self.wrBot.get()
        if texto[:5] == 'media' and texto[:7] != 'mediana':
            lista = [int(x) for x in texto[5:] if x.isnumeric()]
            return self.FuncaoMedia(lista)
        elif texto[:4] == 'moda':
            lista = [int(x) for x in texto[4:] if x.isnumeric()]
            lista.sort()
            return self.FuncaoModa(lista)
        elif texto[:7] == 'mediana':
            lista = [int(x) for x in texto[7:] if x.isnumeric()]
            lista.sort()
            print(lista)
            return self.FuncaoMediana(lista)

    def FuncaoMedia(self, lista):
        media = sum(lista)/len(lista)
        return media

    def FuncaoModa(self, lista):
        return max(lista) #errado

    def FuncaoMediana(self, lista):
        if len(lista)%2==0:
            i = int(len(lista)/2)-1
            return (lista[i]+lista[i+1])/2
        elif len(lista)%2==1:
            i = int(floor(len(lista)/2))-1
            return lista[i]

    def AtivacaoBino(self):
        self.bino = not self.bino
        self.poisson.deselect()
        self.reBot['text'] = 'Modo Binomial'

    def AtivacaoPoi(self):
        self.poi = not self.poi
        self.binomial.deselect()
        self.reBot['text'] = 'Modo Poisson'

    def Funcao(self, texto):
        self.wrBot.delete(0, END)
        self.wrBot.insert(END, texto)



instancia = Tk() #Cria a nossa tela
Calculadora(instancia)

instancia.title('Calculadora Estatística')
instancia.geometry('800x600')
instancia['bg'] = '#E1C2B0'

instancia.mainloop()  #Inicia o programa



