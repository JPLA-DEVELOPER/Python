#-------------------------MAP, FILTER E FUNÇÃO LAMBDA ---------------------------------------------------------------

#---MAP------------------------------------------------------------------------------------------------------------------
#Função do próprio python, utilizada para aplicar funçoes em elementoss de sequência. Dispensa o uso de loop. Econonomiza código.
#Sintaxe: map(função, *sequencia)

#----Sem usar a função MAP--------------------------:
def trata_texto(texto): #Função que vai tratar o texto.
    return texto.replace("'", "").strip()

cadastros =  ["João, 18, jp@gmail.com", #lista
                "Mar'ia, 18, jp@hotmail.com",
              "Pedro, 18, jp@gmail.com"
 ]

resultado = []
for cadastro in cadastros:
    resultado.append(trata_texto(cadastro))

print(resultado)


#-----Usando a função MAP------------------------------:
resultado2 = list(map(trata_texto, cadastros)) #chama a função MAP e passa a função que deve executar(trata_texto) e em qual sequencia de elementos(cadastros).
print(resultado2)


#----FILTER----------------------------------------------------------------------------------------------------------------
#Função do próprio python, é utilizada para filtrar elementos de sequencias que satisfaçam determinadas condições. Dispensa o uso de loop.
#Sintaxe: filter(função, sequencia)




resultado_filter =  list(filter(lambda cadastro: '@gmail' in cadastro, resultado)) # Filtra os cadastros que tenha a string "@gmail"
print(resultado_filter)



#---LAMBDA---------------------------------------------------------------------------------------------------------------
#São pequenas funçõe com apenas uma linha de código. Também chamadas de funções anônimas, por não possuirem nome.
# Sintaxe: lambda argumentos: código

resultado3 = list(map(lambda texto: texto.replace("'", "").strip(), cadastros)) #Cria uma função lambda dentro de um map.
print(resultado3)


#==================================================================================================================================


#---------------------COMPREESÃO DE LISTAS--------------------------------------------------------------------
#Sintaxe: [expressão for item in sequencia if condição] ou [expressão if condição else expressão for item in sequencia]
#Também pode usar de forma aninhada.

emails = ["des@gmail.com",  #Lista
            " sss@gmail.com  ", #espaço em branco
            "fFFff@hotmail.com", #letras maiúsculas
            "ivan2@hotmail.com" #

]

email_tratados = [email.strip().replace(",", "").lower() for email in emails] #Remove espaços em branco, vírgula e transforma tudo em minúscula.
email_tratados_gmail = [email.strip().replace(",", "").lower() for email in emails if '@gmail' in email] #Adiciona um condicional que só retorna os valores corrspondentes a string especificada.


print(f'Emails tratados {email_tratados}')
print(f'Gmails tratados {email_tratados_gmail}')



