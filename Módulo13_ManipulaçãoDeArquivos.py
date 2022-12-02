#Pode ser arquivos binários ou não binários

#--MODOS DE ABERTURA DE ARQUIVOS(Parâmetros) ------
#
# ---------TEXTO---------------------------BINÁRIO
# Leitura: r ou w                             rb ou rb+
# Leitura e Escrita: r+ ou w+                 wb+ ou wb+ 
# Anexaar(append): a ou a+                    ab ou ab+
# 
#

#arquivo = open(caminho, parâmetro)

texto = "Teste de texto"

arquivo = open("C:\\Users\\limaj\\Documents\\GitHub\\Python\Python-2\\ArquivoTeste.txt", "r" )

arquivo.write(texto)
