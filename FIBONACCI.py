NUMERO_TERMOS = int(input('INFORME A QUANTIDADE DE TERMOS DESEJADOS: '))
TERMO_1 = 0
TERMO_2 = 1

print('{','{} - {}'.format(TERMO_1, TERMO_2), end='')

GUIA = 3

while GUIA <= NUMERO_TERMOS:

    TERMO_3 = TERMO_1 + TERMO_2
    print(' - {}'.format(TERMO_3), end='')
    TERMO_1 = TERMO_2
    TERMO_2 = TERMO_3
    GUIA = GUIA + 1

print(' } ESSES SÃO OS ' + str(NUMERO_TERMOS) + ' PRIMEIROS TERMOS.')