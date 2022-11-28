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

    
funcao_com_argumentos(1,2,3,4,5)


print('-------------------------------------------')
def fun_soma(*numeros): #Cria uma função com infinitos parâmetros.
    resultado = 0
    for numero in numeros: #percorre todos eles.
        resultado +=numero #Soma com o próximo.

    return resultado


resultado_soma = fun_soma(1,2,3,4) #Passa 4 argumentos para a função soma.
print(f'Resultado da soma: {resultado_soma}')