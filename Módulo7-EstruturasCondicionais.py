print('\n------CONSULTA APOSENTADORIA-------\n')
idade = input('Digite a sua idade:')
sexo = input('Digite o seu sexo, (M para masculino e F para feminino: ')

if sexo.upper() == 'M' : #Código para o sexo masculino. O ".upper" torna o valor recebido pelo usuário maiúsculo.
    if int(idade) >= 65:
         print('Parabéns! sua aposentadoria já pode ser concedida!')
    else:
         print(f'Negado!! aguarde mais {65 - int(idade)} anos.')





elif sexo.upper() == 'F':     #Código para o sexo feminino. O ".upper" torna o valor recebido pelo usuário maiúsculo.

    if int(idade) >= 60:
        print('Parabéns! sua aposentadoria já pode ser concedida!')
    else:
        print(f'Negado!! aguarde mais {65 - int(idade)} anos.')

else:
    print('Opção inválida, tente novamente!')