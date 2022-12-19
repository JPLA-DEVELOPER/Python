#----------COMPREENSÃO DE DICIONÁRIOS -------------------------------------------------
#Forma consiza de manipular dicionários. Otimiza o seu uso.
#Sintaxe: {chave: valor for elemento in sequencia}


clientes = { #Dicionário.
    'Maria': '041.587.56-85',
    'José': '041.587.56-86',
    'Ana': '041.567.56-88',
    'Marta': '048.587.56-87',
}


#---Forma convencional de fazer----------------------------------------
resultado = {}
for chave, valor in clientes.items():
    resultado[chave] = valor.replace(".", "").replace("-", "") #Elimina as vírgulas e os traços.

print(resultado)

#---Utilizando compreensão de dicionários ----------------------------
resultado2 = {chave: valor.replace(".", "").replace("-", "") for chave, valor in clientes.items()} #Elimina as vírgulas e os traços.
print(resultado2)

#---Com condicional.
resultado3 = {chave: valor.replace(".", "").replace("-", "") for chave, valor in clientes.items() if chave == 'Ana'} #Elimina as vírgulas e os traços e retorna o valor da condicional.
print(resultado3)



