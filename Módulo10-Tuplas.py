#----------------------TUPLAS ---------------------------------------
#--- CARACTERÍSTICAS -----------
#--Ordenados
#--Permite valores duplicados
#--São indexados
#--Permite dados heterogêneos
#--Elementos não-intercambiados(não dá para trocar elementos de lugar dentro de uma tupla)


#--------------------------CRIAÇÃO------------------------------------
tupla = (1, 2, 3,4,5,6,7,8,9,10,11)
print(f'Tupla: {tupla}')

#outra forma de criar tuplas:

lista = [1,2,3,4,5,6,7,8,9,10]
tupla2 = tuple(lista)
print(f'Tupla2: {tupla2}')

#----------Indexação negativa ----------------------------------------
print(f'O quarto elemento da tupla é: {4}') #mostra o elemento que está no índice especificado.


#----------Indexação negativa ----------------------------------------
print(f'O último elemento da lista é: {tupla[-1]}') #Mostra o último elemento da tupla.

#-----------Slicing(fatiamento) --------------------------------------------------
tupla_slicing = tupla[4:] #Faz o fatiamento da tupla pegando do quinto elemento em diante.
print(f'Tupla Slicing: {tupla_slicing}')

#------Deletar com DEL -----------------------------------------------
del tupla[5] #Exclui um valor específico da tupla.
#del tupla #Exclui toda a tupla.
#print(f' Tupla deletada: {tupla}')

#--------------Métodos -----------------------------------------------
print(f'A quantidade de elementos iguais a 1 é: {tupla.count(1)}') #Retorna a quantidade do elemento especificado tem na tupla.
print(f'O elemento 4 está no indice: {tupla.index(4)}') #Retorna em qual posição está o elemento especificado.

#-------------Interação -----------------------------------------------
for elemento in tupla: 
    print(f'Elemento: {elemento}')
