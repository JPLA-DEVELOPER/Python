#-----------------------OPERAÇÕES NUMÉRICAS ----------------------------------------------------
numero_1 = 21
numero_2 = 100
numero_3 = 0.5

print('Soma:', numero_1 + numero_2) # Soma.
print('Subtração: ', numero_1 - numero_2)# Subtração.
print('Multiplicação: ', numero_1 * numero_2) #Multiplicação.
print('Divisão: ', numero_1 / numero_2) #Divisão
print('Resto da divisão: ', numero_2 % numero_1) #Resto da divião(módulo).
print('Exponenciação: ', numero_1 ** 3)# Exponenciação.
print('Divisão arredondada: ', numero_1 // 5) #Divisão arredndada.


# ------------------CONVERSÃO DE TIPOS ------------------------------------------------------------
# str, int, float, complexo.
idade = 26
texto = 'Parabéns joão pelos seus '+ str(idade) +' anos de idade!' #str converte o dado para string. Não é ppossível concatenar strings com outro tipo de dado no meio(converter antes).
print(texto)
pontuacao_str = '10'
print(f'Tipo antes: {type(pontuacao_str)}') # Mostra o tipo de dado antes da conversão.
pontuacao_int = int(pontuacao_str) #int converte a string para inteiro.
print(f'Tipo convertido: {type(pontuacao_int)}') # Mostra o tipo de dado depois da conversão.

print(float(pontuacao_int)) # Converte o inteiro para float.

#----------------IMPORT E MÓDULO MATH ----------------------------------------------------
# help() # faz a consuta da documentação de alguma coisa que tiver dentro do paretese.
# import math #importa tudo o que tem dentro da biblioteca math.
