# faça um programa que leia um nome entre quatro alunos e mostre seu resultado
import random

a= int(input('primeiro nome\n'))
b= int(input('Segundo nome\n'))
c= int(input('terceiro nome\n'))
lista=[a, b, c]
random.shuffle(lista)
print('os nomes adicinados')
print(lista)


