import random
from random import randint
import time
from time import sleep

VALOR_PEDAGIO_CARRO = 3.3 #Contates.
VALOR_PEDAGIO_MOTO = 2.75
VALOR_KM_RODADO_CARRO = 1.5
VALOR_KM_RODADO_MOTO = 1

class Automovel: #classe pai. É abstrata porque não tem a implementação completa de todos os seus métodos.
    numero_total_locacoes = 0 #Cria um atributo de classe que vai ser compartilhado por todas as instancias.
    def __init__(self, montadora, modelo, alugado):
        self.montadora = montadora
        self.modelo = modelo
        self.alugado = alugado
        self.valor_fatura = 0
        self.nome_clientes = "joao"
        print(f'Automóvel {self.montadora} {self.modelo} adquirido pela locadora!')

    def alugar(self, nome_clientes):
        Automovel.numero_total_locacoes += 1 #incrementa 1 ao atributo sempre que o método alugar for chamado.
        self.alugado = True
        self.nome_clientes = nome_clientes
        print(f'O automóvel {self.montadora} {self.modelo} foi alugado por {self.nome_clientes}!!')

    def devolver_automovel(self):
        self.alugado = False
        print(f'O automóvel {self.montadora} {self.modelo} foi devolvido por {self.nome_clientes}!!')
        
    def gerar_valor_fatura(self, numero_pedagios, km_rodados):
        raise NotImplementedError #Quem herdar essa classe que deverá implementar esse método.


    @classmethod
    def mostrar_numero_total_locacoes(cls):
        print(f'O número total de locações de automóveis é de {cls.numero_total_locacoes} locações')

class Carro(Automovel): #Herda a classe Automóvel.
    numero_total_locacoes_carro = 0 #Atributo de classe.
    valor_total_locacoes_carro = 0.0 # Valor arrecadado.
    def __init__(self, montadora, modelo, alugado): #Cria um contrutor referenciando a classe pai.
        super(Carro,self).__init__(montadora, modelo, alugado)
        print("O automóvel adquirido foi um carro!")

    def alugar(self, nome_clientes): #chama o método superior alugar.
        super(Carro,self).alugar(nome_clientes)
        Carro.numero_total_locacoes_carro += 1 #incrementa 1 ao numero de alocações de carro.

    def gerar_valor_fatura(self, numero_pedagios, km_rodados): #Implementa o método não implementado na classe pai
        self.valor_fatura = (numero_pedagios * VALOR_PEDAGIO_CARRO)+(km_rodados * VALOR_KM_RODADO_CARRO)
        Carro.valor_total_locacoes_carro += self.valor_fatura
        print(f'Fatura do carro: {self.montadora} {self.modelo} fatura gerada com sucesso no valor de R${self.valor_fatura:.2f}')

    @classmethod
    def calcular_media_locacoes(cls):
        if cls.numero_total_locacoes_carro != 0:
            media_locacoes_carro = cls.valor_total_locacoes_carro / cls.numero_total_locacoes_carro
            print(f'O valor médio de locação de carros está em R$ {media_locacoes_carro} locações')

        else:
            print('Número total de alucações de carro é igual a 0!')

            
class Moto(Automovel):
    numero_total_locacoes_moto = 0 #Atributo de classe.
    valor_total_locacoes_moto = 0.0 # Valor arrecadado.
    def __init__(self, montadora, modelo, alugado):#Cria um contrutor referenciando a classe pai.
        super(Moto, self).__init__(montadora, modelo, alugado)
        print("O automóvel adquirido foi uma moto!")

    def alugar(self, nome_clientes): #chama o método superior alugar.
        super(Moto,self).alugar(nome_clientes)
        Moto.numero_total_locacoes_moto += 1 #incrementa 1 ao numero de alocações de moto.

    def gerar_valor_fatura(self, numero_pedagios, km_rodados):#Implementa o método não implementado na classe pai
        self.valor_fatura = (numero_pedagios * VALOR_PEDAGIO_MOTO)+(km_rodados * VALOR_KM_RODADO_MOTO)
        Moto.valor_total_locacoes_moto += self.valor_fatura
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





