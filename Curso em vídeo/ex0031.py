'''
ESCREVA UM PROGRAMA QUE LEIA A DISTÃNCIA DE UM USUARIO EM KM,CALCULE O PREÇO DA PASSAGEM COBRANDO
R$0,50 POR KM PARA VIAGENS DE ATÉ 200KM E R$0,45 PARA VIAGENS MAIS LONGAS 
''' 
am = float(input('Quantos km você rodou?:\n'))
if am <= 200:
    print('O valor a ser pago sera...')
    print('{}'.format(am*0.50))   
else:
    print('O valor da passagem sera...')
    print('{}'.format(am*0.45))