from tkinter import *

class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        

        self.titulo = Label(self.primeiroContainer, text="Dados do usuário")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.nomeLabel = Label(self.primeiroContainer,text="Nome", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)

        self.nome = Entry(self.primeiroContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)

        self.senhaLabel = Label(self.primeiroContainer, text="Senha", font=self.fontePadrao)
        self.senhaLabel.pack(side=LEFT)

        

        self.senha = Entry(self.primeiroContainer)
        self.senha["width"] = 30
        self.senha["font"] = self.fontePadrao
        self.senha["show"] = "*"
        self.senha.pack(side=LEFT)

        self.autenticar = Button(self.primeiroContainer)
        self.autenticar["text"] = "Autenticar"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.verificaSenha
        self.autenticar.pack()


        self.senhaLabel = Label(self.primeiroContainer, text="Senhass", font=self.fontePadrao)
        self.senhaLabel.pack(side=LEFT)

        


        self.mensagem = Label(self.primeiroContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

    #Método verificar senha
    def verificaSenha(self):
        usuario = self.nome.get()
        senha = self.senha.get()
        if usuario == "usuariodevmedia" and senha == "dev":
            self.mensagem["text"] = "Autenticado"
        else:
            self.mensagem["text"] = "Erro na autenticação"


root = Tk()
Application(root)
root.mainloop()