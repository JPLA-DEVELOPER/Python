from tkinter import*

janela = Tk()

janela.title(“Insira aqui o seu título“)

texto = Label(janela, text=”Insira aqui o seu texto do botão“)

texto.grid(coluna=0, linha=0, padx=10, pady=10)

botao = Button(janela, text=”Insira aqui a ação do seu botão“, command=acao_botao)

botao.grid(coluna=0, linha=1, padx=10, pady=10)

texto_resposta = Label(janela, text=””)

texto_resposta.grid(column=0, row=2, padx=10, pady=10)

window.mainloop()


numero_1 = input('Digite o primeiro valor:')
numero_2 = input('Didite o segundo valor:')
print('Digite a operação: \n\t + para Adição\n\t - para Subtração\n\t * para Multiplicação\n\t / para Divisão')

operacao = input('Digite a operação desejada:')
equacao = f' {numero_1} {operacao} {numero_2}'
resultado  = eval(equacao) # A função eval recebe "equacao" e processa.
print(f' {"*" * 10}\n Resultado: {resultado}\n {"*" * 10}') # {"*" * 10} imprime 10 *.
