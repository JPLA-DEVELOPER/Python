
#---------------------CLASSE EMPREGADO(PAI)------------------------------------------------

class Empregado:
    numero_empregados = 0 
    def __init__(self, nome_completo, email, matricula_funcional, salario):
        self.nome_completo = nome_completo
        self.email = email
        self.matricula_funcional = matricula_funcional
        self.salario = salario

    
    
    def iniciar_jornada(self, nome_completo, matricula_funcional, salario):
        print(f'O empregado {nome_completo} de matricula {matricula_funcional} e salário {salario} começou a jornada!')
        


    def finalizar_jornada(self, nome_completo, matricula_funcional, salario):
        print(f'O empregado {nome_completo} de matricula {matricula_funcional} e salário {salario} finalizou a jornada!')
        


    def receber_aumento(self, salario_atual, porcentagem_aumento): #método abstrato
        raise NotImplementedError
        



#--------------------------------CLASSE DESENVOLVEDOR(FILHO)-----------------------------------------------


class Desenvolvedor(Empregado):
    porcentagem_aumento = 0

    def __init__(self, nome_completo, email, matricula_funcional, salario):
        super().__init__(nome_completo, email, matricula_funcional, salario)
        print("-------------------------------------")



    def adicionar_linguagem(self, linguagem_programacao, nome_completo):
        lista = ["java", "C", "C#"]
        lista.insert(0, linguagem_programacao)

        print(f'A linguagem {linguagem_programacao} foi adicionada ao desenvolvedor {nome_completo} e sua lista de linguagem é {lista}!!')
        

    def beber_cafe(self, nome_completo, litros_cafe):
        litros_cafe = 2

        print(f'O funcionário {nome_completo} tomou {float(litros_cafe)} de café!!')
        


    def receber_aumento(self,  salario_atual, porcentagem_aumento): #Implementação do método abstrato
        self.salario_com_aumento = (salario_atual) + ((salario_atual) * (porcentagem_aumento/100))
        print(f'O empregado {self.nome_completo} recebeu um aumento de {porcentagem_aumento} % e seu novo salário {self.salario_com_aumento}!')

#--------------------------------CLASSE GERENTE DE PROJETO(FILHO)-----------------------------------------------





desenvolvedor1 = Desenvolvedor("Maria", "maria@gmail.com", "9876543", 1500)


desenvolvedor1.iniciar_jornada("João", "848488822828", 1200)

desenvolvedor1.receber_aumento(1500, 5)

desenvolvedor1.beber_cafe("João", 2)

desenvolvedor1.adicionar_linguagem("Python", "Maria")

desenvolvedor1.finalizar_jornada("João", "848488822828", 1200)






