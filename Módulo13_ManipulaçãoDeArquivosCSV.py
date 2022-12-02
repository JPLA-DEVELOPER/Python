#-------OBJETIVO: exclui o cabeçalho do arquivo e o id, junta o nome e o sobrenome e separa por virgula o email.
resultados = [] #Cria uma lista para guardar os resultados das operações.

with open("C:\\Users\\Same\\Documents\\GitHub\\Python\\Python-1\\cadastro.csv", 'r' ) as arquivo_entrada:#Essa estrutura cria um limitador de contexto. 
#Não precisa usar o closed para fechar.
    linhas = arquivo_entrada.readlines()[1:]#Percorre todas as linhas do arquivo csv. o [1:] remove a primeira linha(cabeçalho).

    for linha in linhas:
        dados = linha.split(',')#Faz a quebra da string por virgula.
        email = dados[3].replace("\n", "") #Substitui o \n por nada.
        resultados.append(f'{dados[1]} {dados[2]}, {email}\n')#Adiciona o valor a lista resultado.

    pass

with open("C:\\Users\\Same\\Documents\\GitHub\\Python\\Python-1\\Saida_cadastro.csv", 'w' ) as arquivo_saida:#Essa estrutura cria um limitador de contexto. 
    for resultado in resultados: #Percorre a lista de valores.
            arquivo_saida.write(resultado) # mostra os valores.