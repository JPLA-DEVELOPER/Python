# FUNÇÃO random.choice: Retorna um valor aleatório dentro de uma sequencia das valores.
# FUNÇÃO string.asci_latters: contem uma sequencia com o alfabeto maiúsculo e minusculo. 
import string
import random

lista = []
tamanho_senha = input("Qual o tamanho da senha? :")
#for i in range(0, tamanho_senha): segunda opção para o laço.
while int(len(lista)) < int(tamanho_senha):
    gerada = random.choice(string.ascii_letters) 
    lista.append(gerada)
    
    
#print(f' Senha gerada: {lista}')
print(f'SENHA GERADA: {"".join(lista)}') #O .join junta todos os elementos da lista semparando por nada. Poderia usar um caractere para separar colocando dentro das "". 