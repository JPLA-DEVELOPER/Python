#------CARACTERÍSTICAS DOS SETS --------
#Elementos sempre desordenados.
#Itens não intercambiáveis(Não dá para trocar itens de lugar dentro de um set).
#Não são idexados(não tem índices para acessar os elementos).
#Não possuem elementos duplicados.
#Possuem métodos para manipulação do conjunto.

#-----SÍNTAXE-------------------------
#nome = {1,2,3} ou 
#nome = set({1,2,3})

set_1 = {'1','2','3'} #Primeira forma de criar um set.
print(f'Set01: {set_1}')

print('\n')

lista = [1,2,3,4]
set_2 = set(lista) #Segunda forma, passando um parâmetro para a função set.
print(f'Set02: {set_2}')

print('\n')

#-----Método ADD -------------
set_1.add('4')#Adiciona um novo valor ao set_1.
print(f'Set01: {set_1}')

print('\n')

#-------------------Método UPDATE ---------------------------
set_1.update('1','2','3','4','5') #Atualiza o set, se não tiver o elemento ele adiciona.
print(f'Set01: {set_1}')

print('\n')

#----------Método DISCARD -----------------
set_1.discard('2') #Descarta o elemento especificado.
print(f'Set01: {set_1}')

print('\n')

#------------Método REMOVE ------------------------
set_1.remove('3') #Remove o elemento desejado, se o elemento não existir ele lança uma excessão.
print(f'Set01: {set_1}')

print('\n')

#-------------Método POP -----------------
item = set_1.pop() #Remove um elemento aleatório do set.
print(f'Foi removido o elemento {item} do Set01 {set_1}')

print('\n')

#-----------Método CLEAR -------------
set_1.clear() #Remove todos os elementos do set.
print(f'Set01: {set_1}')

print('\n')

# -------------OPERAÇÕES MATEMÁTICAS COM SETS ------------------------------
#Novo set:
letras = {'A','B', 'C', 'D', 'E','F'}
vogais = {'A', 'E'}
print(f'Conjunto de letras: {letras}')
print(f'Conjunto de vogais: {vogais}')

print('\n')

#-------INTERSEÇÃO--------------------
intersecao_letras_vogais = letras.intersection() #Pega só os itens que estão em ambos os conjuntos.
print(f'Interseção_Letras_vogais: {intersecao_letras_vogais}')

#---Também pode mostrar os resultados fazendo com o operador de interseção----
# & - interseção.
print(f'Interseção com operador: {letras & vogais}') #Mostra o resultado.

print('\n')

#--------UNIÃO -----------------
uniao_letras_vogais = letras.union() #pega todos os elementos dos dois conjuntos.
print(f'União_Letras_vogais: {uniao_letras_vogais}')

#---Também pode mostrar os resultados fazendo com o operador de união----
# | - união.   
print(f'União com operador: {letras | vogais}') #Mostra o resultado.
print('\n')

#------DIFERENÇA ---------------
diferenca1_letras_vogais = letras.difference(vogais) #Mostra todos que estão em letras que n ão estão em vogais.
diferenca2_letras_vogais = vogais.difference(letras) #Mostra todos 

print(f'Letras - vogais: {diferenca1_letras_vogais}')
print(f'Vogais - letras: {diferenca2_letras_vogais}')

#---Também pode mostrar os resultados fazendo com o operador da diferença simétrica----
# ^ - diferença simétrica.
print(f'Diferença com operador: {letras - vogais}') #Mostra o resultado.
print('\n')

#-------DIFERENÇA SIMÉTRICA ------------------
#Se adicionar o Update ele vai alterar o conjunto de origem.
#Itens que estão em um dos dois conjuntos, mas não estão em ambos(retira a interseção).
simetrica_letras_vogais = letras.symmetric_difference(vogais)
print(f'Simétrica: {simetrica_letras_vogais}')

#---Também pode mostrar os resultados fazendo com o operador da diferença----
# - - diferença.
print(f'Diferença simétrica com operador: {letras ^ vogais}') #Mostra o resultado.

print('\n')

#--------------------MÉTODOS DE CONJUNTOS -------------------------
print(F'Os conjuntos letras e vogais são separados: {letras.isdisjoint(vogais)}') #Verifica se são conjuntos disjuntos(separados, sem interseção)
print(F'O conjunto letras pertence ao conjunto vogais : {letras.issubset(simetrica_letras_vogais)}') #Verifica se todos os elementos de um conjunto estão dentro de outro.
print(F'O conjunto letras é um super conjunto de vogais: {letras.issuperset(vogais)}') #Verifica se um conjunto é um superset de outro.
 
