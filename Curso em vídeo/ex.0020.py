# faça um programa que leia um nome entre quatro alunos e mostre seu resultado
from random import shuffle

a= str(input('primeiro nome\n'))
b= str(input('Segundo nome\n'))
c= str(input('terceiro nome\n'))
lista=[a, b, c]
shuffle(lista)
print('os nomes adicinados')
print(lista)


