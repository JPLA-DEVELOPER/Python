
#list = []
lista =[0,"str", 5,5, []] #Declara e preeche a lista com tipos de dados variados.
print(lista) #mostar a lista inteira.

for elemento in lista: #Laço de repetição que mostra cada elemento da listga.
    print(f'O elemento atual é: {elemento}')


#-------EXEMPLOS -------------

pares = [2,4,6,8]
impares = [1, 3, 5, 7]

print(f'Na posição {pares[0]} o valor é: {pares[0]}')
soma = pares[1] + impares[3]
print(f'Soma é igual a: {soma}')
print(pares[-1]) #Mostra o último elemento da lista. Útil para descobrir qual o último elemento da lista.


from random import randint # Importa a biblioteca randint.
alunos = ['João', 'Pedro', 'José', 'Amanda']

for boletim in alunos:
    nota = randint(7, 10)
    print(f'O nome do aluno é {boletim} a nota foi: {nota}')
  

#-------------------------------------

nomes = ['João', 'Pedro', 'José', 'Amanda']
peso = [randint(7, 10), randint(7, 10), randint(7, 10), randint(7, 10)]

print('\n')

for valor, peso in zip(nomes, peso): #Lê mais de uma lista de uma vez.
    print(f'Nome {valor} tem peso: {peso}')

print('\n')

#----------------FATIAMENTO DE LISTAS (SLICING) -----------------
#lista = [índice de início da string, indice do fim da string, de quantos]
#          0    1    2    3   4    5
letras = ['a', 'b', 'c', 'd','e', 'f']
#         -5   -4   -3   -2  -1    0

print(f'Primeira parte: {letras[0: 3: 1]}') # lista[inicio: fim da primeira parte + 1: de quantos em quantos]
print(f'Segunda parte: {letras[3: 6: 1]}') # lista[inicio: fim da segunda parte + 1: de quantos em quantos]

print('\n')
print(f'Primeira parte: {letras[-6:-3:1]}')# lista[inicio da primeira parte - 1: vazio : de quantos em quantos]
print(f'Segunda parte: {letras[-3::1]}')# lista[inicio da segunda parte - 1: fim da primeira parte(ordem invertida): de quantos em quantos]

print('\n')
#------INVERTER UMA LISTA ------------------------------
print(f'Lista invertida: {letras[::-1]}')#Percorre a lista de trás pra frente.

print('\n')

#------PEGAR ELEMENTOS SALTANDO UM LISTA ---- - - - - -
print(f'Lista saltada: {letras[::2]}') #Como não é definido o começo nem o fim, ele percorre a lista do começo ao fim saltando 2.

#------CONCATENAR ELEMENTOS DE DUAS LISTAS -------------------
print(f'Concatenação: {letras[::2] + letras[1::2]}') 





#-------------MANIPULAÇÃO DE LISTAS ---------------------------
sacola = ['Feijão', 'Arroz', 'Sal', 'Açucar', 'Café']
print(f'A lista é: {sacola}')

print('\n')

#Método APPEND(objeto).
sacola.append('Macarrão') #Adiciona o item macarão na lista.
print(f'A nova lista é: {sacola}') #Mostra a lista com o novo elemento.

#Método EXTEND(Estrutura)
sacola.extend(['Biscoito', 'Farinha', 'Carne'])  #Adiciona uma outra lista no final da lista atual.
print(f'A nova lista é: {sacola}') #Mostra a lista com os novos elementos.

#Método ISERT(índice(posição), objeto)
sacola.insert(0, 'milho') #Insere um novo elemento numa posição específica.
print(f'A nova lista é: {sacola}') #Mostra a lista com os novos elementos.

#Método REMOVE(objeto)
sacola.remove('Macarrão') #Remove o item Macarrão.
print(f'A nova lista é: {sacola}') #Mostra a lista com os novos elementos.


#Método POP(índice)
sacola.pop(3) #Remove o item da posição desejada da lista e o retorna. Caso o índice não seja especificado, retorna o último elemento.
print(f'A nova lista é: {sacola}') 

#Método CLEAR()
#sacola.clear() #Remove todos os elementos da lista.
#print(f'A nova lista é: {sacola}')

#método INDEX(valor[comeco, fim]) #Os parâmetros permitem que seja definido um intervalo de valores para a busca.
print(sacola.index('Café')) #Retorna o índice do primeiro elemento do vetor especificado.
print(f'Lista após a chamada do método INDEX(): {sacola}')


#Método COUNT(valor)
sacola.count('Café') #Conta o número de ocorrências do valor especificado na lista.
print(f'Lista após a chamada do método COUNT(): {sacola}')

#Método SORT(chave, reverso)
sacola.sort(reverse =True) #Ordena os ítens da lista. Parâmetros adicionais podem ser adicionados para customizar.
print(f'Lista após a chamada do método SORT(): {sacola}')

#Método REVERSE()
sacola.reverse() #Reverte os elementos da lista.
print(f'Lista após a chamada do método REVERSE(): {sacola}')

#Método COPY()
copia_sacola = sacola.copy() #Faz uma cópia dos elementos da lista na mesma ordem
print(f'Lista após a chamada do método COPY(): {copia_sacola}')