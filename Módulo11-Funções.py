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

def calculo_media_mediana(notas): #função.
    media = sum(notas)  / len(notas) #sum faz a soma do valores de uma lista, len conta a quantidade de valores da lista.
    if len(notas) % 2 == 0:
    
    else:
    notas_ordenadas = sorted(notas) #ordena a lista em ordem crescente.
    indice_mediana = in(len(notas)/2)

    return media


resultado = calculo_media_mediana([10,8,4]) #Passa como argumento para a função uma lista de notas.
print(f'Média: {resultado}')