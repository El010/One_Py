'''
Faça um programa que leia um numero 9999 e mostre na tela cada um dos digitos separados
 ex: digite um numero
 unidade 
 dezena 
 centena 
 milhar 
 '''
numero=int(input('enter a value or numbers: '))
u = numero // 1 % 10 # recebe o valor divide por 1 e pega o resto
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10   
print('the value your enter has {} UNIT'.format(u))
print('TEN UNID {}'.format(d))
print('HUNDRED {}'.format(c))
print('THOUSAND {}'.format(m))