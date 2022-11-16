numero_1 = input('Digite o primeiro valor:')
numero_2 = input('Didite o segundo valor:')
print('Digite a operação: \n\t + para Adição\n\t - para Subtração\n\t * para Multiplicação\n\t / para Divisão')

operacao = input('Digite a operação desejada:')
equacao = f' {numero_1} {operacao} {numero_2}'
resultado  = eval(equacao) # A função eval recebe "equacao" e processa.
print(f' {"*" * 10}\n Resultado: {resultado}\n {"*" * 10}') # {"*" * 10} imprime 10 *.
