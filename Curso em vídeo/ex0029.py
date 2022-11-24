'''
ESCREVA UM PROGRAMA QUE LEIA A VELOCIDADE DE UM CARRO, SE ELE UTRAPASSAR 80KM MOSTRE UMA MESSAGEM DIZENDO
QUE ELE FOI MULTADO
A MULTA CUSTARA R$7,00 REAIS, POR CADA KM ACIMA DO LIMITE 
'''
am=float(input('A quantos km você está? '))
if am >= 80:
    print('você utrapassou limite')
    print('valor da multa {:.2f}'.format())
else:
    print('tudo certo')

