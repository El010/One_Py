# Faça um programa que recebe três valores, e sortei um aleatoriamente

from random import random
aluno1=str(input('nome do primeiro alunon(a)\n'))
aluno2=str(input('nome do segundo aluno(a)\n'))
aluno3=str(input('terceiro aluno(a)\n'))
aluno4=str(input('Quarto aluno:\n'))
lista=[aluno1, aluno2, aluno3, aluno4]
escolhido=random.choised(lista)
print('O aluno escolhido foi {}'.format(escolhido))


# erro
