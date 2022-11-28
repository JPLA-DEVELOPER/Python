from random import randint
def sorteio(intervalo_inferior, intervalo_superior, quantidade_de_valores):

    
    lista = []
    for i in range(intervalo_inferior, quantidade_de_valores, 1):
        
        sorteado = randint(intervalo_inferior, intervalo_superior)
        repetidos = lista.count(sorteado)
        if repetidos == 0:
            lista.insert(0, sorteado)
            print(lista)
        elif repetidos != 0:
            print('valor repetido!')
            #quantidade_de_valores = (quantidade_de_valores - 1)
            q = len(lista)
        return q  


print(f'Lista: {lista} ')



sorteio.
sorteio(1, 10, 10)
