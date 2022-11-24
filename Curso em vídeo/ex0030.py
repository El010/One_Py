'''
CRIE UM PROGRMA QUE LEIA UM NUMERO QUALQUER, E MOSTRE SE ELE E PAR OU IPAR
'''
numb1=int(input("Digite um numero "))
if (numb1 % 2) == 0: # O resto e arredondado, se ele nao tiver resto sempre vai ser par 
    print( 'Par')
else:
    print('Seu número e impar')
print('{}'.format(numb1 % 2))
