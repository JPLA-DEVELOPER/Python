#----------CORRESPONDÊNCIA DE PADRÕES PATTERN MATCHING--------------
#TÉCNICA INTRODUZIDA ATRAVÉS DAS peps 634, 635 e 636.

#Muitos denominam a técnica como o switch/case que o python nunca teve, mas o casamento de padrões é muito mais que isso.
#Só está presento no python 3.10 ou superior.


#Sintaxe: match expressão:
#          case padrao1:
#               bloco de código para o padrão 1.
#          case padrao2:
#               bloco de código para o padrão 2.
#         
#        Outros padrões...
#        case_:
#                bloco de código quando nenhum padrão for satisfeito

# TIPOS DE PADRÕES:
#Padrões literais.
#Padrão Coringa.
#Padrões de sequência.
#Padrões de Mapas.
#Padrões de Classes.
#Padrões de captura.
#Padrões de OR.
#Padrões AS.


#---PADRÕES LITERAIS--------------
genero = "M"
match genero:
    case "M":
        print("gerero masculino")
    case "F":
        print("gerero feminino")



idade = 15
match idade:
    case x if x <18:#com comparação
        print("Menor de idade")
    case x if x > 18:
        print("Maior de idade")



#---PADRÃO CORINGA--------------------------
genero = "X"
match genero:
    case "M":
        print("gerero masculino")
    case "F":
        print("gerero feminino")
    case _: #Se nenhum bloco anterior for executado.
        print("genero incorreto, tente novamente!")


#--PADRÃO DE SEQUÊNCIA-------------------------

notas = [5,8,6]

match notas:
    case[]:
        print("Aluno não realizou nenhuma prova")
    case[p1]:
        print(f"Aluno faltou duas provas. sua média é {p1/3:.2f}")
    case[p1, p2]:
        print(f"Aluno faltou duas provas. sua média é {p1+ p2/3:.2f}")
    case[0, *resto]:
         print(f"Aluno zerou a primeira prova e suas notas foram {resto}")

    case[p1, p2,p3]:
        print(f"A média final é {(p1+ p2+ p3)/3:.2f}")



#--PADRÕES DE MAPAS ----------------------------------------------
produtos = [
    {"nome": "Teclado", "valor": 789, "categoria": "computador"},
    {"nome": "Teclado", "valor": 789, "categoria": "computador"},
    {"nome": "Teclado", "valor": 789, "categoria": "eletrodomestico"}

]

for produto in produtos:
    match produto:
        case{"nome": nome, "valor": valor, "categoria": "computador"}:
            print(f'O produto {nome} está com um mega desconto de' f'20%: de R$ {valor} por {valor*0.8:.2f}')
        case{"nome": nome, "valor": valor, "categoria": "eletrodomestico"}:
            print(f'O produto {nome} está com um mega desconto de' f'20%: de R$ {valor} por {valor*0.8:.2f}')


#--PADRÃO DE CLASSES- ------------------

class Carro:
    def __init__(self, montadora, modelo):
        self.montadora = montadora
        self.modelo = modelo

carro = Carro(montadora= "tesla", modelo = "model S")#instancia a classe.

match carro:
    case Carro(montadora= "Ford", modelo = "Fiesta"):
        print("Ford fiesta")
    case Carro(montadora= "Fiat", modelo = "Pulse"):
        print("Fiat Pulse")
    case Carro(montadora= "tesla", modelo = "model S"):
        print("Tesla")

        

#--PADRÕES DE CAPTURA --------------------------------------
#Utilizado anteriormente nos padrões de sequ~encia.


# ---PADRÕES OR --------------------------------------------


 notas = [0.0,8,6]

match notas:
    case[]:
        print("Aluno não realizou nenhuma prova")
    case[p1]:
        print(f"Aluno faltou duas provas. sua média é {p1/3:.2f}")
    case[p1, p2]:
        print(f"Aluno faltou duas provas. sua média é {p1+ p2/3:.2f}")
    case[0 | 0.0, *resto]: #O | permite um ou outro.
         print(f"Aluno zerou a primeira prova e suas notas foram {resto}")

    case[p1, p2,p3]:
        print(f"A média final é {(p1+ p2+ p3)/3:.2f}")


#---PADRÃO AS -----------------------------------

match notas:
    case[]:
        print("Aluno não realizou nenhuma prova")
    case[p1]:
        print(f"Aluno faltou duas provas. sua média é {p1/3:.2f}")
    case[p1, p2]:
        print(f"Aluno faltou duas provas. sua média é {p1+ p2/3:.2f}")
    case[0 | 0.0, *resto] as lista: #O AS permite apelidar o caso.
        print(f'Primeira nora: {lista[0]}')
        print(f"Aluno zerou a primeira prova e suas notas foram {resto}")

    case[p1, p2,p3]:
        print(f"A média final é {(p1+ p2+ p3)/3:.2f}")