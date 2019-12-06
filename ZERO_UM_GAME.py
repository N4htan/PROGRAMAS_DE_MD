A = input('INFORME A JOGADA DE A: ')
B = input('INFORME A JOGADA DE B: ')
C = input('INFORME A JOGADA DE C: ')

if A != B and A != C:
    print('A É O VENCEDOR')

elif B != A and B != C:
    print('B É O VENCEDOR')

elif C != A and C != B:
    print('C É O VENCEDOR')

else:
    print('TENTEM NOVAMENTE, NINGUEM GANHOU')
