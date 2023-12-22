# 1) Métodos de Tk()
# --> minsize
# --> maxsize

# 2) Grid
# --> widget.grid(row = linha, column = coluna) (posição do widget)
# --> columnspan/rowspan = colunas/linhas que ele pode ocupar
# --> sticky = N/W/E/S = posicionamento do widget com relação a uma célula
# --> pad =
# --> grid_forget(pack_forget)


from tkinter import *

class Imagem(object):
    def __init__(self):
        self.root = Tk()
        self.root.geometry("400x100")
        self.root.minsize(width=400, height=100)  # tamanho minimo
        self.root.maxsize(width=600, height=400)  # tamanho maximo
        self.root.title('Final')

        # Depois criamos o label altura
        self.a = Label(self.root, text="Altura: ")
        self.a.grid(row=0, sticky=E)

        # E o label largura
        self.l = Label(self.root, text="Largura: ")
        self.l.grid(row=1, sticky=E)

        # Criamos as duas entradas para dados
        self.e1 = Entry(self.root)
        self.e2 = Entry(self.root)
        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)

        # O botão que verifica se deve-se ou não preservar o aspecto
        self.p = Checkbutton(self.root, text="Preserva Aspecto")
        self.p.grid(columnspan=2, sticky=E)
        self.prv = False

        # E a imagem que nós devemos colocar
        self.imagem = Label(self.root, bg='black')
        self.imagem.grid(row=0, column=2, columnspan=5, rowspan=2)

        self.root.mainloop()

Imagem()

