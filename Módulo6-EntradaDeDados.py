#nome = input('Qual é o seu nome:') # Lê do usuário o dado.
numero = input('Qual o número: ') #Lê o número do usuário.
expoente = input('Qual o expoente: ') #Lê o expoente do usuário.

resultado = int(numero) ** int(expoente) # Converte os strings lidas em inteiro e faz a operação.
print(f'Resultado de {numero} elevado a {expoente} é igual a: {resultado}') #Mostra o valor lido.
