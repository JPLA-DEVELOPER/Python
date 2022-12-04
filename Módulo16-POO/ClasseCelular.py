class Celular: #cria uma classe celular
    def __init__(self, fabricante, modelo, tela, armazenamento, memoria, camera, bateria, tela_ligada): #Contrutor da classe com seus atributos. Faz a inerface com o mundo externo.
        self.fabricante = fabricante
        self.modelo = modelo
        self.tela = tela
        self.armazenamento = armazenamento
        self.memoria = memoria
        self.camera = camera
        self.bateria = bateria
        self.tela_ligada = tela_ligada




        #print("o conrutor __init__ foi chamado!")    
    def ligar_tela(self): #Método, 
        self.tela_ligada = True


celular_android = Celular("Samsung", "J2", 6.25, 128, 4,21, 3400, False) #Cria um método celular android para instanciar a classe celular e passa os argumentos de modo sequencial.
celular_android2 = Celular(fabricante = "Samsung", modelo ="J2", tela = 6.25, armazenamento = 128, memoria = 4, camera = 21, bateria = 3400, tela_ligada = False) #Cria um método celular android2 para instanciar a classe celular e passa os argumentos de modo nomeado.


celular_android2.tela_ligada = True #modifica o valor do atributo para True.
print(celular_android2.tela_ligada)#imprime o atributo tela_ligada do método celular_android2.