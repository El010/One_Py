# Faca um programa que leia o comprimento do cateto oposto e do cateto adjecente de um triãngulo 
# retângulo, calcule e mostre o comprimento da hípotenusa
###### lógica ####
# peça o  valor do cateto oposto
# peca o valor do cateto adjecente 
# faca a somatoria 
# mostre o resultado formatado

am=float(input(f'Valor do cateto oposton\n'))
ma=float(input(f'Valor do cateto adjacente\n'))
sm= am**2 + ma**2 + (1/2)
print('O valor da hipotenusa é {}²\n'.format(sm))

### resolução da aula 
import math
v1=float(input('valor do cateto oposto:'))
v2=float(input('Valor do cateto adjacente:'))
v3=math.hypot(v1, v2)
print('A hipotenusa vai medir {:.2f}'.format(v3))

### IMPORTANDO APENAS UMA FUNÇAÕ DA BIBLIOTECA, PARA OCUPAR MENOS ESPAÇO NA MEMORIA DO PC ##
from math import hiport
vm = float(input("valor do cateto: "))
mv = float(input(' Valor do cateto: '))
vs= hiport(vm, mv)
print('O resultado da hipotenusa é {}'.format(vs))