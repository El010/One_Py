# Faça um programa que recebe três nomes, e sortei um aleatoriamente

from random import choice
aluno1=str(input('nome do primeiro alunon(a)\n'))
aluno2=str(input('nome do segundo aluno(a)\n'))
aluno3=str(input('terceiro aluno(a)\n'))
lista=[aluno1, aluno2, aluno3]
escolhido=choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
