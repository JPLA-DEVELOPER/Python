#------COMPREENSÃO DE SETS -------------
class Pessoa:
    def __init__(self, nome, idade, cidade, genero):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade
        self.genero = genero

    def __repr__(self):
        return f"Pessoa: {self.nome}"

pessoas = [
    Pessoa("João", 20, "Belém", "M"),
    Pessoa("Catarina", 24, "Belém", "F"),
    Pessoa("Ana", 25, "Fortaleza", "F"),
    Pessoa("Joana", 40, "Belém", "F"),
    Pessoa("Alberto", 30, "Rio", "M")
]

cidades = {pessoa.cidade for pessoa in pessoas}
print(cidades)#Mostra os elementos não repetidos.

pessoas_iniciadas_com_j = {pessoa for pessoa in pessoas if pessoa.nome[0] == "J"}
print(pessoas_iniciadas_com_j)#

pessoas_maior_30 = {pessoa for pessoa in pessoas if pessoa.idade > 30}
print(pessoas_maior_30)

pessoas_sexo_masculino = {pessoa for pessoa in pessoas if pessoa.genero.upper() == "M"}
print(pessoas_sexo_masculino)