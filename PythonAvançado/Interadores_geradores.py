# ----------INTERADORES E GERADORES -----------------------------------------------------------------



#-------------------INTERADORES ----------------------------------------------------
#INTERÁVEIS: São objetos que podem ser utilizados em estruturas de repetição. Ex: listas, sets, tupls e dicionários.
#INTERADORES:São objetos utilizados para se interr sobre iteráveis(como percorrer cada elemento da estrutura). São criados coma função iter() do Python.

#Protocolo Iterator: adicionado através da PEP 243 e facilita a criação de iteradores. Para usar devemos desenvolver um classe que implemente os seguintes métodos:
#   __inter__(): Esse método deve retornar self.
#   __next__(): Esse método deve retornar o próximo valor da sequência. Ao chegar ao final dela, deve lançar uma exceção StopInteration.



#--------------------GERADORES -------------------------------------------------------
#Facilitam a implementação do protocolointerator, pois podemos desenvolver interadores sem a necessidade de classes para tal.
#Para criar geradores, utilizamos a notação de definião de funções (def) mas ao invés de utilizar o return, utilizamos a palavra reservada yield.
# São estruturas muito perfomáticas






lista = [1, 2, 3, 4, 5]
interador_lista = iter(lista) #chama a função interador e passa o argumento lista.
print(next(interador_lista))


class NumerosPares: #Classe que implementa o protocolo Interator do python.
    def __init__(self, maximo, atual):
        self.maximo = maximo
        self.atual = 0

    def __inter__(self):
        return self

    def __next__(self):
        if self.atual > self.maximo:
            raise StopIteration

        retorno = self.atual
        self.atual += 2
        return retorno


interador_numeros_pares = NumerosPares(maximo = 150)
for numero in interador_numeros_pares:
    print(numero, end = "")


#-------GERADORES------------------------------------------------
def numeros_pares(maximo):
    atual = 0

    while atual < maximo:
        yield atual #Retona o primeiro elemento da sequencia.

        atual += 2 #