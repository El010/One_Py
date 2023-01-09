'''
FAÇA UM PROGRAMA QUE LEIA UM ANO QUALQUER E MOSTRE SE ELE E BISSEXTO
'''
a=int(input('Entre com um numero de ano: '))
if ( a % 4 == 0  and a % 100!=0) or (a%400==0):
    print('bissexto')
else:
    print('Não bissexto')
# and a%100!=0) or (a%400==0):