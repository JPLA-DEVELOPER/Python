# FUNÇÃO random.choice: Retorna um valor aleatório dentro de uma sequencia das valores.
from random import  randint
import random
import time
print('----------------------SORTEIO----------------------------------------------------\n\t')


lista = [] #Lista que vai guardar os valores sorteados.
intervalo_inferior = int(input("Intervalo inferior:"))
intervalo_superior = int(input("Intervalo superior:"))
quantidade_numeros = int(input("Quantos números deseja sortear dentro desse intervalo? :"))
#for i in range(0, quantidade_numeros): segunda opção para o laço.
while len(lista) < quantidade_numeros:
    numero_sorteado = random.randint(intervalo_inferior, intervalo_superior) #gera um valor aleatório dentro do intervalo
    lista.append(str(numero_sorteado)) #converte o numero sorteado para string e adiciona na lista.
    
print("\n-----------------RESULTADO:---------------")


contador = 6 #Numero de segundos
while contador: 
        mins, secs = divmod(contador, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        #print(timer, end="\r") 
        time.sleep(1) 
        contador -= 1
        print(f'Divulgação do resultado em: {contador} segundos')

print(f'\nNÚMEROS SORTEADOS: {", ".join(lista)}\n') #O .join junta todos os elementos da lista semparando por nada. Poderia usar um caractere para separar colocando dentro das "". 