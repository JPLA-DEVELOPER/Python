#Pode ser arquivos binários ou não binários

#--MODOS DE ABERTURA DE ARQUIVOS(Parâmetros) ------

#------------------------TABELA DE MÓDULOS ----------------------------
# ---------TEXTO(legivel)---------------------BINÁRIO(inlegível)-------------------
# Leitura: r. Leitura/escrita:r+                 rb  e  rb+
# Escrita: w. Escrita/Leitura: w+                wb+ e  wb+ 
# Anexaar(append): a. Anexar/Ler: a+             ab e ab+
# 


#arquivo = open("caminho", 'parâmetro')


#---------------------CRIAR ARQUIVO E ESCREVER NELE --------------------------------

texto = "Teste de escrita de texto em arquivo"

arquivo = open("C:\\Users\\Same\\Documents\\GitHub\\Python\\Python-1\\ArquivoTeste.txt", 'w' )#Cria um arquivo de texto no caminha epecificado

arquivo.write(texto) #Escreve o texto da variavel texto no arquivo.

arquivo.close() #Fecha o arquivo aberto. Sempre tem que ser utilizada.

print("\n\t------------------------------------------------------------------------------------")

#---------------------LER O ARQUIVO -------------------------------------

arquivo = open("C:\\Users\\Same\\Documents\\GitHub\\Python\\Python-1\\ArquivoTeste.txt", 'r' )#O parâmetro r faz a leitura.

retorno = arquivo.read() #Ler o texto.
print(f'Texto escrito no arquivo: {retorno}')
arquivo.close()
print("\n\t------------------------------------------------------------------------------------")

#-----------------------------ANEXAR(APPEND) TEXTO EM UM ARQUIVO-----------------------------------------------
novo_texto = "\nTexto anexado"
arquivo = open("C:\\Users\\Same\\Documents\\GitHub\\Python\\Python-1\\ArquivoTeste.txt", 'a' )#O parâmetro anexa texto ao arquivo.

arquivo.write(novo_texto) #Escreve o novo texto na função.
arquivo.close() #fecha o arquivo.
print("\n\t------------------------------------------------------------------------------------")




#--------------------LEITURA DE ARQUIVOS BINÁRIOS -----------------------------------------------------------------------------------------------
arquivo_png = open("C:\\Users\\Same\\Documents\\GitHub\\Python\\Python-1\\luaPNG.png", 'rb' )
retorno_png = arquivo_png.read() #Ler o arquivo binário.
print(f'O arquivo PNG é: {retorno_png}') #Mostra os códigos binários do arquivo.
arquivo_png.close()

#---------------DUPLICANDO UM ARQUIVO BINÁRIO ------------------------------
arquivo_png_original = open("C:\\Users\\Same\\Documents\\GitHub\\Python\\Python-1\\luaPNG.png", 'rb' ) #Abre o arquivo binário a ser copiado.
retorno_png_cópia = arquivo_png_original.read() #Ler os códigos binários do arquivo a ser copíado.

arquivo_png_copiado = open("C:\\Users\\Same\\Documents\\GitHub\\Python\\Python-1\\COPIAluaPNG.png", 'wb' ) #Cria um novo arquivo de texto no endereço e nome especificado.
arquivo_png_copiado.write(retorno_png_cópia) # Copia os códigos binários lidos e adiciona ao novo arquivo de texto.
arquivo_png.close()#Fecha