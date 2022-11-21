cadastro = {  #Declara um dicionário chamado cadastro e preenche com diversos tipos de dados distintos..
'id': 1565,
'nome': 'João Paulo Lima',
'filhos': ['Joana', 'Mateus'],
'compras': [{ #Lista contendo outros dicionários dentro.
    'id': 999000,
    'produto': 'Notebook',
    'preco': 2.578
}, {
    'id': 898500,
    'produto': 'Monitor',
    'preco': 1.578
}]

}

print(f'Dicionário Cadastro:{cadastro}\n') #Imprime todo o dicionário.

print(cadastro['id']) #mostra o valor da variável id.


print(f'Usuário: {cadastro["nome"]} \nFez as compras: {cadastro["compras"][0]}\n') # Imprime o elemento especificado pelo dicionário, índice do dicionário e elemento da lista dentro do dicionário.

#Outra forma de resgatar os dados do dicionário.
usuario = cadastro['nome']
compra = cadastro['compras'][0]
print(f'Usuário: {usuario} fez as compras: {compra}')


# ----------------Método de acesso GET -----------------------------

cadastro_usuario = cadastro.get('nomee', None) #Faz o acesso do elemento especificado no primeiro parâmetro e caso não exista retorna o valor definido no segundo parâmetro.
print(f'Nome: {cadastro_usuario}')


#--------NOVO DICIONÁRIO -----------------------------------------------------------------------------

computador = {
'cpu': 'Core i7',
'ram': 'DDR 16Gb',
'ssd': 'Samsung Evo',
'gpu': 'RTX 2080'
}

print(f'Computador 01: {computador}') #Mostra o dicionário computador.

#----ACESSA, MODIFICA E ADICIONA O VALOR DE UMA DETERMINADA CHAVE DO DICIONÁRIO ---------------------
computador['ram'] = 'DDR4 32Gb' #Acessa e modifica.
computador['fonte'] = 'Fonte 6000' #Adiciona um lovo elemento no dicionário.
print(f'Computador 01: {computador}') #Mostra o dicionário computador depois da atualização do dado "ram".

print('\n') 
#-----Atualizando e adicionando com o método UPDATE.
computador.update({'estabilizador': 'Estabilizador', 'fonte' : 'Fonte 850 W', 'ssd': 'SSD 500Gb'}) #Consegue adicionar, atualizar e adicionar vários elementos ao mesmo tempo.
print(f'Computador 02: {computador}')


#---------Função DELL para excluir elementos de um dicionário-------------------
del computador['cpu'] # Exclui o valor referente ao índice cpu.
print(f'Computador 03: {computador}')


# ---------Método POP para excluir elementos-------------
computador.pop('ram') #Exclui o elemento especificado.
print(f'Computador 04: {computador}')

# ---------Método POPITEM para excluir elementos-------------
computador.popitem() #Exclui sempre o último elemento do dicionário.
print(f'Computador 05: {computador}')

#--------------Função CLEAR ----------------------
#computador.clear() #Exclui todos os elementos do dicionário.
#print(f'Computador 06: {computador}')
  

  #--------------Função COPY -------------------------
itens = computador.copy()#Copia o dicionário inteiro.
print(f'Itens_computador_copiado: {itens}')

#--------------Função KEYS ---------------------------
chave = computador.keys() #Retorna todas as CHAVES( não os valores)) em forma de lista.
print(f'Chaves: {chave}')

#----------ITENS
itens = computador.items() #Retorna os pares chave(chave e valor): valor em formato de lista.
print(f' Itens: {itens}')

#-------------Função VALUES ---------------------------
valores = computador.values() #Retorna todos os VALORES(não a chave) em formato de lista.
for valor in valores: #Percorre toda a lista e exibe os valores.
  print(f'\tValores: {valor} ')


#----------SETDEFAULT------------------
#Isere a chave com o valor passado SE a chave não estiver presente no dicionário e
#retorna o valor da chave SE a chave já estiver presente no dicionário.
computador.setdefault('ssd', 'SSD Kink 1T') #Primeiro parâmetro é a chave a ser procurada e o segundo o valor a ser inserido se a chave ainda não existir no dicionário.
print(f' Computador: {computador}')

# ------FROMKEYS -----------------------------

chavess = ['Mãe', 'Pai', 'Filho', 'Filha']
valorr = 0 #Valor que vai ser atribuido a todas as chaves.

jogo = dict.fromkeys(chavess, valorr) #Cria um dicionário a partir de lista de chaves e valores.
print(F'Jogo: {jogo}')


