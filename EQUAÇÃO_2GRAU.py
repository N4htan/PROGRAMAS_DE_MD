a = (int(input("INFORME UM VALOR INTEIRO PARA 'a': ")))
b = (int(input("INFORME UM VALOR INTEIRO PARA 'b': ")))
c = (int(input("INFORME UM VALOR INTEIRO PARA 'c': ")))

DELTA = (b * b) - (4 * a * c)

if DELTA >= 0:

    RAIZ_DELTA = DELTA ** 0.5
    X1 = - (b - RAIZ_DELTA) / (2 * a)
    X2 = - (b + RAIZ_DELTA) / (2 * a)

    if X1 == X2:
        print("O VALOR DE X E IGUAL A " + str(X1))
    else:
        print("O VALOR DE X1 E IGUAL A " + str(X1) +  " E O VALOR DE X2 E IGUAL A " + str(X2))

else:

    print("O VALOR DE Δ E " + str(DELTA) + " MENOR QUE 0 PORTANTO, NÃO PODEMOS PASSAR PARA O PROXIMO PASSO.")



