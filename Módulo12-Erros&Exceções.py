#-----------TIPOS DE ERRROS ------------------------------------

# ZeroDivisionError: Tentar fazer uma divisão por zero.
# NameError: Nome de variável errado.
# TypeError: Operação entre tipos não suportados(dividir uma string por um inteiro).
# IndentationError: Erro de indentação do código.



def divide_dois_numeros(dividendo, divisor):
    return dividendo / divisor


try: 
    #Código a ser testado. Se ele retornar um erro a axceção será chaamada.7
    
    numero_1 = int(input('Digite o primeiro número: '))
    numero_2 = int(input('Digite o segundo número: '))
    resultado = divide_dois_numeros(numero_1, numero_2)

    print(resultado)

except TypeError:  #Especifica a exceção 
    #Executa esse código casa um esse tipo de erro ocorra.
    print('Um erro ocorreu! tipo não suportadado')

except ZeroDivisionError as variavel_a_guardar_erro:  #Especifica a exceção e uma variável para guardar o seu tipo.
    #Executa esse código casa esse tipo de erro ocorra.
    print(f'Um erro ocorreu! divisão por zero não suportada {variavel_a_guardar_erro}')


else: #execute esse código caso nenhum erro ocorra.
    print(resultado)

finally: #Sempre executa esse código.

    print('Finalizando o programa, Obrigado!')




print('\n------------------------------------------------------------------------------------')

    #------------------------------------LANÇAMENTO DE EXEÇÃO COM RAISE-----------------------------------------------------------------


cadastro_csv = [
    'João, 28i, Analista de sistemas',
    'Maria, 31, Desenvolvedor frontend',
    'Jonas, 37, Gerente de projetos',
    'Alberto, 47' #erro
]


def processa_dados(cadastro):
    for cadastro in cadastro: #Percorre a lista.
        dados = cadastro.split(',') #Separa os valores separados por vírgula.


        if len(dados) != 3: # Verifica a quantidade de elementos em cada passo da lista.
            raise ValueError('formato incorreto dos dados') #se a quantidade for diferente de 3 é lançado um erro.
             #O rais permite que quem chamar a função vai conseguir identificar e tratar o erro facilmente(basicameno troca a mensaggem de erro padrão por uma mais bonita).

        nome = dados[0] #Guarda os valores separados.
        try:
            idade = dados[1]#Guarda os valores separados.
        except ValueError:
            raise ValueError('Erro no formato do dado idade!') #lança uma exceção.
        
        cargo = dados[2]#Guarda os valores separados.

        print(f'{nome} tem {idade} anos e exerce o cargo de {cargo}')
         


try:
    processa_dados(cadastro_csv) 

except ValueError as excecao:
    print(f'O programa encontrou um erro: {excecao}')