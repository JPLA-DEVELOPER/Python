import random
from random import randint
import time
from time import sleep

VALOR_PEDAGIO_CARRO = 3.3 #Contates.
VALOR_PEDAGIO_MOTO = 2.75
VALOR_KM_RODADO_CARRO = 1.5
VALOR_KM_RODADO_MOTO = 1

class Automovel: #classe pai. É abstrata porque não tem a implementação completa de todos os seus métodos.
    def __init__(self, montadora, modelo, alugado):
        self.montadora = montadora
        self.modelo = modelo
        self.alugado = alugado
        self.valor_fatura = 0
        self.nome_clientes = "joao"
        print(f'Automóvel {self.montadora} {self.modelo} adquirido pela locadora!')

    def alugar(self, nome_clientes):
        self.alugado = True
        self.nome_clientes = nome_clientes
        print(f'O automóvel {self.montadora} {self.modelo} foi alugado por {self.nome_clientes}!!')

    def devolver_automovel(self):
        self.alugado = False
        print(f'O automóvel {self.montadora} {self.modelo} foi devolvido por {self.nome_clientes}!!')
        
    def gerar_valor_fatura(self, numero_pedagios, km_rodados):
        raise NotImplementedError #Quem herdar essa classe que deverá implementar esse método.



class Carro(Automovel): #Herda a classe Automóvel.
    def __init__(self, montadora, modelo, alugado): #Cria um contrutor referenciando a classe pai.
        super(Carro,self).__init__(montadora, modelo, alugado)
        print("O automóvel adquirido foi um carro!")

    def gerar_valor_fatura(self, numero_pedagios, km_rodados): #Implementa o método não implementado na classe pai
        self.valor_fatura = (numero_pedagios * VALOR_PEDAGIO_CARRO)+(km_rodados * VALOR_KM_RODADO_CARRO)
        print(f'Fatura do carro: {self.montadora} {self.modelo} fatura gerada com sucesso no valor de R${self.valor_fatura:.2f}')


class Moto(Automovel):
    def __init__(self, montadora, modelo, alugado):#Cria um contrutor referenciando a classe pai.
        super(Moto, self).__init__(montadora, modelo, alugado)
        print("O automóvel adquirido foi uma moto!")

    def gerar_valor_fatura(self, numero_pedagios, km_rodados):#Implementa o método não implementado na classe pai
        self.valor_fatura = (numero_pedagios * VALOR_PEDAGIO_MOTO)+(km_rodados * VALOR_KM_RODADO_MOTO)
        print(f'Fatura da moto: {self.montadora} {self.modelo} fatura gerada com sucesso no valor de R${self.valor_fatura:.2f}')   



def mostrar_fatura(automovel):#função polimorfica.
    print(f'O valor da fatura do automovel {automovel.modelo}  alugado por {automovel.nome_clientes} ficou no valor de R${automovel.valor_fatura:.2f}')
    


#------------------------------------USAR AS CLASSES:--------------------------------------------------------------------------------

#ALUGA
fiesta = Carro("Fornd", "Fiesta", "False") #carro
fiesta.alugar("João")

honda_cb = Moto("Honda", "CB500", False)#moto
honda_cb.alugar("Ana")


#TEMPO ALUGADO
sleep(randint(7,10)) #Simulação de tempo de aluguel(pausa a execução por um instante). gera um valor eleatório de tempo em segundos.

#DEVOLVE
fiesta.devolver_automovel() #carro
honda_cb.devolver_automovel()#moto

#GERAR FATURA
fiesta.gerar_valor_fatura(numero_pedagios = 5, km_rodados= 750)#carro
mostrar_fatura(fiesta)

honda_cb.gerar_valor_fatura(numero_pedagios= 5, km_rodados= 400)#moto
mostrar_fatura(honda_cb)





