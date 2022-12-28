#Strings podem ser declaradas com a função str ou com aspas
sexo = str('Masculino')
nome = 'João Paulo'
sobrenome = 'Lima'
idade = 25.24

print(f'Sexo é: {sexo} ')
print(nome+ ' ' + sobrenome) #concatena as duas strings deixando um espaço entre elas.
nome_completo = nome+ ' ' + sobrenome # Junta as duas strings em uma nova variável.
print(nome_completo.upper())# upper() torna todos os caracteres da string e transfrma em maiúsculo,lower() torna minúsculo.
print(nome_completo.strip())# remove espaços em branco antes da string.
print(nome_completo + '\n  Quebra de linha. \n\t Dá um tab.')
print(' \'printa as aspas simples\'')

print('Meu nome é:{nome} e meu sobrenome é:{sobrenome} e a idade {idade}'.format(nome = nome, sobrenome = sobrenome, idade = idade)) #O .format mostra o valor da variável exatamente onde tem as {} na ordem definida.
print('idade: {idade:.1f}\n\n'.format(idade = idade)) # .1f manipula a quantidade de numeros após o ponto.


# --------------------   F-STRINGS  --------------------------------

titulo = 'monitor'
tamanho = '27'
preco = 1.200
tipo = 'produto'

print(f'{tipo.upper():_^50}') # imprime o valor da variável maiúscula e com 50 - 7 = 43 caracteres *. O ^ centraliza o nome entre os caracteres(<>, alinha a direira e a esquerda).
print (

    f'Título: {titulo}\n'
    f'Tamanho: {tamanho}\'\n'
    f'Valor: R$ {preco:.3f}\n'
)


# --------------------   FUNÇÕES DE STRINGS ----------------------------------------

print( 'strip ' .strip(titulo)) # remove os espaços em branco.
print(f'título:  {titulo.upper()} tamamnho: {titulo.lower()}') # .upper = maiúsculo, .lower = minúsculo.
print('Remo,ver, virgu,las, e subtituir, por alguma, cois,a' .replace(',', ''))# substitui ","(alguma coisa) por nada ou outra coisa.
print('conta a quantide de letras "As" presentes aqui nessa frase!'  .count('a'))# Conta a quantidade de caracteres escohido.
print('Centralizar texto' .center(50, '*') ) # Cenraliza o texto e preeche o restante de espaços com asterisco.
print('Mostra o index da posição do cractere procurado' .index('i'))# mostra a posição do caractere.
print('numérico?' .isnumeric()) # retorna se o valor é alfanumérico ou não.
print("quebra onde tem espaço(ou outro caractere) e passa para uma lista" .split(' '))# quebra de texto feita onde tem um determinado caractere.
print('título da página' .title())# Torna os primeiros caracteres das strings miúsculas.
print('título da pagina' .capitalize()) # Transforma apenas o primeiro caractere da string em maiúsculo.
print('444' .zfill(5)) # Completa a string até chegar em 5 caracteres com zeros a esquerda.
string_extensa = 'essa string é muito grande'
print(len(string_extensa)) # A função "len()" mostra o tamanho da string.


#----INTEROLAÇÃO DE STRINS COM %---------------------
#String------%s
#Inteiro-----%i ou %d
#Float-------%f
#
varialvel_de_interpolacao = 'o nome é %s e a idade é %.2f anos' %(nome, idade) # % e o tipo dedados e depois valores.
print(varialvel_de_interpolacao)


# ------------------ENCADEAMNTO DE FUNÇÕES ---------------------------
print(' te;x;;to  '.strip().replace(';', '').center(25,'*').upper())


# ---------------- ÍNDICE DE STRINGS ------------------------------
nome = 'João Paulo Lima'
print(nome[3]) #retorna o caractere correspondente ao índice 3.
print(nome[-1]) #Indexação negativa que retorna o indice em ordem contrária, nesse caso retornará o último elemento da string.
print(nome[-1] == 'a') #verifica se o último elemento da string é um "a".
