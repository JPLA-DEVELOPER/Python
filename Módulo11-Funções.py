#-------------------------FUNÇÕES --------------------------------
# Parâmetro vai na função e o argumento vai no chamado da função.
# O retun não é obrigatório numa função.
def funcao(nome, idade, emprego): #Declara afunção e passa 3 parâmetros.
    print(f'Olá, meu nome é {nome} Minha idade é {idade} sou {emprego}') #Mostra os valores.

funcao('João', '25', 'Desenvolvedor') #chama a função e passa argumentos para serem processados pela função.
funcao('Maria', '29', 'Desenvolvedor')


#----------------------------------------------------------------------------------------------------
def fun2(valor_1, valor_2): #Declara a função 
    soma = valor_1 + valor_2
    
    return soma


resultado = fun2(10, 20) #Argumentos passados para a função calcular.
print(resultado)



#-----------------------------------------------------------------------------
print('\t----------------------NOVA FUNÇÃO--------------------------\n\t')
def calculo_media_mediana(notas): #Declara a função.
    media = sum(notas)  / len(notas) #sum faz a soma do valores de uma lista, len conta a quantidade de valores da lista.
    if len(notas) % 2 == 0: #Se número pá de elementos.
       # O pass permite  execução do if sem executar nada.
        indice_central_menor = int(len(notas)/2-1) # Descobre o índice do menor elemento central.
        indice_central_maior = int(len(notas)/2) #Descobre o índice do maior elemento central.
        ponto_central_menor = notas[indice_central_menor] #Retorna para a variável o valor correspondente ao índice descoberto.
        ponto_central_maior = notas[indice_central_maior] #Retorna para a variável o valor correspondente ao índice descoberto.

        mediana = (ponto_central_menor + ponto_central_maior) / 2 #Descobre a mediana.
        
    else: #Se número ímpar de elementos.
        notas_ordenadas = sorted(notas) #A função sorted ordena a lista em ordem crescente.
        indice_mediana = int(len(notas)/2) #Tranforma para interio e divide por 2 para retornar a mediana.
        mediana = notas_ordenadas[indice_mediana]
    
    return media, mediana #Retorna esses valores para quem chamar a função.




resultado_media, resultado_mediana = calculo_media_mediana([10,8,4,9,5,2]) #Duas variáveis recebendo a função. Passa como argumento para a função uma lista de notas.
print(f'Média: {resultado_media}\n Mediana: {resultado_mediana}')





print('-------------------PARÂMETROS POSICIONAIS-------------------------')


def funcao_com_argumentos(arg1, arg2, *args): #A notação *args permite adicionar infinitos argumentos para a função.
    print(f'Arg1: {arg1}')
    print(f'Arg2: {arg2}')
    print(f'Args: {args}')

    
funcao_com_argumentos(1,2,3,4,5) #Mostra os valores na ordem definida aqui.


print('-------------------------------------------')
def fun_soma(*numeros): #Cria uma função com infinitos parâmetros.
    resultado = 0
    for numero in numeros: #percorre todos eles.
        resultado +=numero #Soma com o próximo.

    return resultado


resultado_soma = fun_soma(1,2,3,4) #Passa 4 argumentos para a função soma.
print(f'Resultado da soma: {resultado_soma}')


print('\n\t-------------------------------------------')
def fun2_soma(maximo, *numeros): #Cria uma função com infinitos parâmetros, mas que vai obedecer um valor máximo definido dentro da função.
    resultado = 0
    numeros_somados= [] #Cria uma lista para guardar os valores somados.
    
    for numero in numeros: #percorre todos eles.
        if(resultado + numero) > maximo:
            break #Para a execução se a condição for satisfeita.

        resultado +=numero #Soma com o próximo.
        numeros_somados.append(numero) #Adiciona o número somada ao final da lista.

    return resultado, numeros_somados #Retorna o resultado das somas e a lista de valores somados.


resultado_soma2 = fun2_soma(100, 5,68,30,40) #Passa 5 argumentos para a função soma, sendo que o primeiro é o valor máximo.
print(f'Resultado da soma: {resultado_soma2}')



print('\n\t-----------------------------------PARÂMETROS NOMEADOS--------------------------------------------------------------')

def monta_computador(cpu, memoria, hd, monitor):
    print(f'O computaodr montado foi:')
    print(f'CPU: {cpu}')
    print(f'Memória: {memoria} Gb')
    print(f'HD: {hd} TB')
    print(f'Monitor: {monitor} '' ')


monta_computador('core i7', monitor = 24, memoria = 16, hd = 1) #define(liga) cada argumento ao seu respectivo valor independente da posição. Pode misturar parâmetros posicionais com nmeados, desde que os posicionais venham antes dos nomeados.


print('\n\t-----------------------------------PARÂMETRO COM VALOR PADRÃO--------------------------------------------------------------')

def monta_computador(cpu, memoria, hd, monitor = 32): #define um valor padrão para o parâmetro monitor.
    print(f'O computaodr montado foi:')
    print(f'CPU: {cpu}')
    print(f'Memória: {memoria} Gb')
    print(f'HD: {hd} TB')
    print(f'Monitor: {monitor} '' ')


monta_computador('core i7', memoria = 16, hd = 1) #Não está parssando nenhum parâmetro para monitor e ele está pegando o valor padrão.



print('\n\t-----------------------------------PARÂMETRO NOMEADOS NÃO DEFINIDOS--------------------------------------------------------------')
#------------------------ORDEM: POSICIONAIS -> POSICIONAIS VARIAVEIS -> NOMEADOS -> NOMEADOS VARIAVÉIS 

def monta_computador(cpu, memoria, hd, monitor = 32, **kwargs): #todos os argumentos nomeados vão cair aqui no parâmetro kwargs.
    print(f'O computaodr montado foi:')
    print(f'CPU: {cpu}')
    print(f'Memória: {memoria} Gb')
    print(f'HD: {hd} TB')
   # print(f'Outros atributos: {kwargs} '' ')

    for chave, valor in kwargs.items(): #Percorre os parâmetros peado cada chave e valor e imprime.
        print(f'Atributo {chave} : {valor}')




monta_computador('core i7', memoria = 16, hd = 1, webcam = 'Multilaser', teclado = 'LG') #Os cois últimos argumentos vão ser assados para o parâmetro não definido akwargs.


#------------------------------------------------------------------------------------------------------------------

print('---------------------------TYPE HINTS-----------------------------------')

def aplica_baskhara(a: float, b: float, c: float) -> (float, float): #diz que quem jchamar a função deve esperar dois float como retorno.
    delta = b ** 2 - 4 * a * c 
    x_1 = (-b + ( delta ** 1/2) / (2 * a))
    x_2 = (-b - ( delta ** 1/2) / (2 * a))

    return x_1, x_2 #mutlipos retotnos.

def aplica_desconto(produtos:dict, desconto: float) -> dict: #dict deixa claro que a vriável produtos é do tipo dicionário e descontodo tipo float. -> diz que a função retorna o tipo dicionário.
    resultado = {}
    for nome_produto, valor in produtos.items():
        resultado[nome_produto] = (f'{valor*(1-desconto):.2f}') #calcula o desconto ara cada item do dicionário. retorna formatado com 2 casas decimais.

    return resultado

valores_produtos = { #Dicionário de itens.
    'microondas': 497.99,
    'computador': 3499.97,
    'forno': 399.97

}




print(aplica_desconto(valores_produtos, 0.15)) #retorna os valores dos produtos presentes no dicionários com os descontos.
print(aplica_baskhara(5.0, 15.0,-25.0))