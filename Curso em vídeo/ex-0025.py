'''
crie um programa que leia o nome de uma pessoa e diga se o nome tem SILVA ou não
'''
nome=str(input('Qual seu nome: \n')).strip().lower()
print('Seu nome nome tem SILVA ?\n {}'.format('silva' in nome))