from random import  randint

print('------------SORTEIO--------------')


lista = []

#valor = input('Escolha uma valor entre 1 e 10:')

for i in range(1, 200, 1): #Começa em 1 e vai percorrendo até o 11 passandode um por um.
    sorteado = randint(1, 10) #Gera um número aleatório entre 1 e 10.
    
    quantidade = lista.count(sorteado) #Conta quantos elementos com o valor sorteados tem na lista.
    if quantidade == 0:
       # print(f'Quantidade: {quantidade}')
        #print(f'O valor sorteado {sorteado} já está na lista!!\n')
        

        #elif quantidade == 0:
        #print(f'Quantidade: {quantidade}')
        lista.insert(0, sorteado) #Insere o valor gerado na lista sempre no índice 0.
        q = len(lista) #Mostra a quantidade de elementos da lista.
        print(f'O {i}º número  sorteado é {sorteado} a Lista de sorteados fica: {lista}\n')


