#Primeiro código Python

"""
As aspas triplas permitem escrever texto em várias linhas. OB: não é considerado comentário.
"""

print('Hello World!!')
nome = 'jp'
sobrenome = 'lima'
idade = 26
altura = 1.63

print(12, 13, 14, sep= "--")# O sep= insere um separador especificado entre os argumentos não nomeados, nesse caso é o --.
print(12, 13, 14, end= "@") #Acidiona um @ ao final da impressão.
print(type(nome))

print( nome + sobrenome) # Concatena as duas strings.
print(f' Meu nome é {nome} e meu sobrenome é {sobrenome} e minha idade é {idade} e minha altura é {altura}!') # o "f" permite a inserção de texto com estrings.



