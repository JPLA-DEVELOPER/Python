import Empregado

class Desenvolvedor(Empregado):
    porcentagem_aumento = 10

    def __init__(self, nome_completo, email, matricula_funcional, salario):
        super(Empregado, self).__init__(nome_completo, email, matricula_funcional, salario)
        print("-------------------------------------")



    def adicionar_linguagem(self, linguagem_programacao, nome_completo):
        lista = []
        lista.append(linguagem_programacao)
        print(f'A linguagem {linguagem_programacao} foi adicionada ao desenvolvedor {nome_completo} e sua lista de linguagemé {lista}!!')
        

    def beber_cafe(self, nome_completo, litros_cafe):
        litros_cafe = 2

        print(f'O funcionário {nome_completo} tomou {float(litros_cafe)} de café!!')
        


    def receber_aumento(self, nome_completo, matricula_funcional, salario, porcentagem_aumento): #Implementação do método abstrato
         
        salario_com_aumento = (salario) + ((salario) * (porcentagem_aumento/100))

        print(f'O empregado {nome_completo} de matricula {matricula_funcional} recebeu um aumento de {porcentagem_aumento} % e seu novo salário {salario_com_aumento}!')
