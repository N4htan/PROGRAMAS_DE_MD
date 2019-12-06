NUMERO = int(input("DIGITE UM NUMERO PARA CALCULAR O FATORIAL: "))
CALCULO = NUMERO
GUIA = 1

print('CALCULANDO {}! = '.format(NUMERO), end='')

while CALCULO > 0:

    print('{}'.format(CALCULO), end='')
    print(' x ' if CALCULO > 1 else ' = ', end='')
    GUIA *= CALCULO
    CALCULO -= 1
print('{}'.format(GUIA))