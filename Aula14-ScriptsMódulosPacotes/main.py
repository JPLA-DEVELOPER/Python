
# import matematica: importa tudo.
# from matematica import*: importa tudo. Não é uma boa pratica se o módulo for muito grande pq vai importar muita coisa desnecessária.
# from matematica import soma, subtracao: so importa a função especificada do módulo matemática. Nesse caso não precisa colocar o módulo no momento de chamar, chama só a função.
# from matematica import soma as funcao_de_soma: Nesse caso(o "as") ele dá um apelido para a função soma.

import matematica #importa tudo que está presente no módulo matemática.
from operacoes.soma import soma_dois_numeros #faz a importação de uma função que está dentro de um módulo que está dentro de um pacote.
print(matematica.soma(1,2)) #Chama o função soma do módulo matematica e mostra o resultado.
print(matematica.subtração(5,2)) #Chama o função subtração do módulo matematica e mostra o resultado.

print(soma_dois_numeros(2, 49))
