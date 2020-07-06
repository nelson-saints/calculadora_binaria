import os
import math
while True:
    try:
        operacao = input('Operação entre números binários: \n [1]: Soma \n [2]: Subtração \n [3]: Multiplicação \n [4]: Divisão \n [5]: Módulo \nQual operação matemática você quer fazer? \n R: ')
        operacao = int(operacao)
    except ValueError:
        print('Opção Inválida!!!')
    if operacao not in [ 1, 2, 3, 4, 5 ]:
        print('Entre com as expressões informadas!!!')
    else:
        try:
            n1 = int(input('Entrada 1: '),2)
            n2 = int(input('Entrada 2: '),2)
        except ValueError:
            print('**ERRO ENTRE COM NÙMEROS EM FORMATO DE BINÀRIO**')
            os._exit(0)
        if operacao == 1:
            total = n1 + n2
            print('Total: ','{:0>8}'.format(bin(total)[2:]))
            os._exit(0)
        elif operacao == 2:
            total = n1 - n2
            print('Total: ','{:0>8}'.format(bin(total)[2:]))
            os._exit(0)
        elif operacao == 3:
            total = n1 * n2
            print('Total: ','{:0>8}'.format(bin(total)[2:]))
            os._exit(0)
        elif operacao == 4:
            total = n1 / n2
            print('Total: ','{:0>8}'.format(bin(total)[2:]))
            os._exit(0)
        elif operacao == 5:
            total = math.floor(n1 % n2)
            print('Total: ','{:0>8}'.format(bin(total)[2:]))
            os._exit(0)
