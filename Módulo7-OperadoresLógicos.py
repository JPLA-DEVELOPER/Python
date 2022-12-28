#---------OPERADOR LÓGICO ------------------------
x = True
y = False

#0, 0.0, '' São por adrão False.

print('*** IS ***')
print(x is y)
print( True is False)

#---AND(E)-------
# F F = F
# F T = F
# T F = F
# T T = T

print('*** AND ***')
print(False and False)
print(False and True)
print( True is False)
print(True and True)

#----OR(OU)--------
# F F = F
# F T = T
# T F = T
# T T = T

print('*** OR ***')
print(False or False)
print(False or True)
print( True or False)
print(True or True)

# -- NOT(NÃO) ------ Inverte os valores lógicos das variáveis.
print('*** NOT ***')
print(not True)
print(not False)


#-----OPERADOR IN-------------- Verifica se o valor especificado está no interavel.
#-----OPERADOR NOT IN-------------- Verifica se o valor especficado NÂO está no interável.

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome: #Verifica se a string encontrar está em nome.
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')

# ------------OPERADORES DE COMPARAÇÃO ----------------------------------

# == Igualdade.
# =! Diferente.
# > Maior.
# < Menor.
# >= Maior ou igual.
# <= Menor ou igual.

#-----------OPERADORES DE ATRIBUIÇÃO ---------------------------------------

# x += 10 (Equivale a x = x+10)
# x -= 10 (Equivale a x = x-10)
# x /= 10 (Equivale a x = x/10) Divisão arredondada
# x *= 10 (Equivale a x = x*10)
# x %= 10 (Equivale a x = x%10) Resto da divisão.

