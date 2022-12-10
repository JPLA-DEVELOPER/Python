
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
        

    def receber_aumento(self, nome_completo, matricula_funcional, salario): #método abstrato
        raise NotImplementedError 
        



#empregado1 = Empregado("João","jpla@gmail.com", "848488822828", 1200)
#desenvolvedor1 = Desenvolvedor("Java", "Maria")

#empregado1.iniciar_jornada("João", "848488822828", 1200)
#empregado1.receber_aumento("João", "848488822828", 1200)
#empregado1.finalizar_jornada("João", "848488822828", 1200)






