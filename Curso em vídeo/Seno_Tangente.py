# Faça um programa que leia um ângulo qualquer, e mostre se seno,cosseno, e tangente desse ângulo
import math
angulo=float(input('Qual o valor do ângulo:\n'))
seno=math.sin(math.radians(angulo))
cosseno=math.tan(math.radians(angulo, seno))
a = math.cos(math.radians(angulo, cosseno))
# O seno, representado como (sin) estava passando o valor de 'x' em graus radiano
# no caso foi usado outra função para ele tranformar o valor pedido do programa em centigrados 'radinas'
print('O ângulo {} tem o seno {}'.format(angulo, seno))
