#-------------------PRIMEIRA FORMA FOR-------------------------
sequencia = [1, 2, 3] # A variável sequencia recebe uma lista de 3 elementos.
for elemento in sequencia: #A cada interação a variável elemento vai receber um valor da lista.
    print(f'{elemento}')


# -----------------SEGUNDA FORMA FOR-------------------------------------
for i in range(0, 10, 1): # "i" é uma variável qualquer. O primeiro parãmetro da função range é de onde começa o valor de i, o segundo até onde vai e o terceiro a condição de avanço.
    print(f' O valor de i é: {i}')


#-------------------- WHILE ----------------------

from random import randint #Importa a função randint.
capacidade_maxima_do_balde = 1000
balde = 0

while balde <= capacidade_maxima_do_balde:
    volume_copo = randint(95, 100) #Passa para a variável "volume_balde" a função randint que gera uma valor aleatório entre 95 e 100.
    print(f'O copo foi enchido com: {volume_copo} mls')
    balde += volume_copo

    print(f'Volume do balde: {balde} mls\n')
    print(f'O volume do balde utrapassou a capacidade máxima de: {capacidade_maxima_do_balde} mls e está com { balde} mls')
